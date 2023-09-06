	
import pandas as pd
from datetime import datetime,timedelta



#Abro los ficheros con los que voy a tratar




df_vulnibm_iot = pd.read_excel('vulnerabilidades_ibm_iot_2023.xlsx')

#Variable para almacenar el contador total de valores de puntuacion temporal
count_vulnibm_iot_tempscore=0

#Variables para almacenar el contador total de un valor concreto de puntuacion temporal
count_vulnibm_iot_tempscore_10=0
#Variables para almacenar la suma de valor de PUNTUACION BASE para calcular la media dada una puntuacion temporal especifica
count_vulnibm_iot_tempscore_10_risklevel=0
#Variable para almacenar el contador total de un PUNTUACION BASE dada una puntuacion temporal especifica
count_vulnibm_iot_tempscore_10_risklevel10=0
count_vulnibm_iot_tempscore_10_risklevel9=0
count_vulnibm_iot_tempscore_10_risklevel8=0
count_vulnibm_iot_tempscore_10_risklevel7=0
count_vulnibm_iot_tempscore_10_risklevel6=0
count_vulnibm_iot_tempscore_10_risklevel5=0
count_vulnibm_iot_tempscore_10_risklevel4=0
count_vulnibm_iot_tempscore_10_risklevel3=0
count_vulnibm_iot_tempscore_10_risklevel2=0
count_vulnibm_iot_tempscore_10_risklevel1=0
count_vulnibm_iot_tempscore_10_risklevel0=0



count_vulnibm_iot_tempscore_9=0
count_vulnibm_iot_tempscore_9_risklevel=0
count_vulnibm_iot_tempscore_9_risklevel10=0
count_vulnibm_iot_tempscore_9_risklevel9=0
count_vulnibm_iot_tempscore_9_risklevel8=0
count_vulnibm_iot_tempscore_9_risklevel7=0
count_vulnibm_iot_tempscore_9_risklevel6=0
count_vulnibm_iot_tempscore_9_risklevel5=0
count_vulnibm_iot_tempscore_9_risklevel4=0
count_vulnibm_iot_tempscore_9_risklevel3=0
count_vulnibm_iot_tempscore_9_risklevel2=0
count_vulnibm_iot_tempscore_9_risklevel1=0
count_vulnibm_iot_tempscore_9_risklevel0=0


count_vulnibm_iot_tempscore_8=0
count_vulnibm_iot_tempscore_8_risklevel=0
count_vulnibm_iot_tempscore_8_risklevel10=0
count_vulnibm_iot_tempscore_8_risklevel9=0
count_vulnibm_iot_tempscore_8_risklevel8=0
count_vulnibm_iot_tempscore_8_risklevel7=0
count_vulnibm_iot_tempscore_8_risklevel6=0
count_vulnibm_iot_tempscore_8_risklevel5=0
count_vulnibm_iot_tempscore_8_risklevel4=0
count_vulnibm_iot_tempscore_8_risklevel3=0
count_vulnibm_iot_tempscore_8_risklevel2=0
count_vulnibm_iot_tempscore_8_risklevel1=0
count_vulnibm_iot_tempscore_8_risklevel0=0

count_vulnibm_iot_tempscore_7=0
count_vulnibm_iot_tempscore_7_risklevel=0
count_vulnibm_iot_tempscore_7_risklevel10=0
count_vulnibm_iot_tempscore_7_risklevel9=0
count_vulnibm_iot_tempscore_7_risklevel8=0
count_vulnibm_iot_tempscore_7_risklevel7=0
count_vulnibm_iot_tempscore_7_risklevel6=0
count_vulnibm_iot_tempscore_7_risklevel5=0
count_vulnibm_iot_tempscore_7_risklevel4=0
count_vulnibm_iot_tempscore_7_risklevel3=0
count_vulnibm_iot_tempscore_7_risklevel2=0
count_vulnibm_iot_tempscore_7_risklevel1=0
count_vulnibm_iot_tempscore_7_risklevel0=0


count_vulnibm_iot_tempscore_6=0
count_vulnibm_iot_tempscore_6_risklevel=0
count_vulnibm_iot_tempscore_6_risklevel10=0
count_vulnibm_iot_tempscore_6_risklevel9=0
count_vulnibm_iot_tempscore_6_risklevel8=0
count_vulnibm_iot_tempscore_6_risklevel7=0
count_vulnibm_iot_tempscore_6_risklevel6=0
count_vulnibm_iot_tempscore_6_risklevel5=0
count_vulnibm_iot_tempscore_6_risklevel4=0
count_vulnibm_iot_tempscore_6_risklevel3=0
count_vulnibm_iot_tempscore_6_risklevel2=0
count_vulnibm_iot_tempscore_6_risklevel1=0
count_vulnibm_iot_tempscore_6_risklevel0=0


count_vulnibm_iot_tempscore_5=0
count_vulnibm_iot_tempscore_5_risklevel=0
count_vulnibm_iot_tempscore_5_risklevel10=0
count_vulnibm_iot_tempscore_5_risklevel9=0
count_vulnibm_iot_tempscore_5_risklevel8=0
count_vulnibm_iot_tempscore_5_risklevel7=0
count_vulnibm_iot_tempscore_5_risklevel6=0
count_vulnibm_iot_tempscore_5_risklevel5=0
count_vulnibm_iot_tempscore_5_risklevel4=0
count_vulnibm_iot_tempscore_5_risklevel3=0
count_vulnibm_iot_tempscore_5_risklevel2=0
count_vulnibm_iot_tempscore_5_risklevel1=0
count_vulnibm_iot_tempscore_5_risklevel0=0


count_vulnibm_iot_tempscore_4=0
count_vulnibm_iot_tempscore_4_risklevel=0
count_vulnibm_iot_tempscore_4_risklevel10=0
count_vulnibm_iot_tempscore_4_risklevel9=0
count_vulnibm_iot_tempscore_4_risklevel8=0
count_vulnibm_iot_tempscore_4_risklevel7=0
count_vulnibm_iot_tempscore_4_risklevel6=0
count_vulnibm_iot_tempscore_4_risklevel5=0
count_vulnibm_iot_tempscore_4_risklevel4=0
count_vulnibm_iot_tempscore_4_risklevel3=0
count_vulnibm_iot_tempscore_4_risklevel2=0
count_vulnibm_iot_tempscore_4_risklevel1=0
count_vulnibm_iot_tempscore_4_risklevel0=0

count_vulnibm_iot_tempscore_3=0
count_vulnibm_iot_tempscore_3_risklevel=0
count_vulnibm_iot_tempscore_3_risklevel10=0
count_vulnibm_iot_tempscore_3_risklevel9=0
count_vulnibm_iot_tempscore_3_risklevel8=0
count_vulnibm_iot_tempscore_3_risklevel7=0
count_vulnibm_iot_tempscore_3_risklevel6=0
count_vulnibm_iot_tempscore_3_risklevel5=0
count_vulnibm_iot_tempscore_3_risklevel4=0
count_vulnibm_iot_tempscore_3_risklevel3=0
count_vulnibm_iot_tempscore_3_risklevel2=0
count_vulnibm_iot_tempscore_3_risklevel1=0
count_vulnibm_iot_tempscore_3_risklevel0=0


count_vulnibm_iot_tempscore_2=0
count_vulnibm_iot_tempscore_2_risklevel=0
count_vulnibm_iot_tempscore_2_risklevel10=0
count_vulnibm_iot_tempscore_2_risklevel9=0
count_vulnibm_iot_tempscore_2_risklevel8=0
count_vulnibm_iot_tempscore_2_risklevel7=0
count_vulnibm_iot_tempscore_2_risklevel6=0
count_vulnibm_iot_tempscore_2_risklevel5=0
count_vulnibm_iot_tempscore_2_risklevel4=0
count_vulnibm_iot_tempscore_2_risklevel3=0
count_vulnibm_iot_tempscore_2_risklevel2=0
count_vulnibm_iot_tempscore_2_risklevel1=0
count_vulnibm_iot_tempscore_2_risklevel0=0

count_vulnibm_iot_tempscore_1=0
count_vulnibm_iot_tempscore_1_risklevel=0
count_vulnibm_iot_tempscore_1_risklevel10=0
count_vulnibm_iot_tempscore_1_risklevel9=0
count_vulnibm_iot_tempscore_1_risklevel8=0
count_vulnibm_iot_tempscore_1_risklevel7=0
count_vulnibm_iot_tempscore_1_risklevel6=0
count_vulnibm_iot_tempscore_1_risklevel5=0
count_vulnibm_iot_tempscore_1_risklevel4=0
count_vulnibm_iot_tempscore_1_risklevel3=0
count_vulnibm_iot_tempscore_1_risklevel2=0
count_vulnibm_iot_tempscore_1_risklevel1=0
count_vulnibm_iot_tempscore_1_risklevel0=0

count_vulnibm_iot_tempscore_0=0
count_vulnibm_iot_tempscore_0_risklevel=0
count_vulnibm_iot_tempscore_0_risklevel10=0
count_vulnibm_iot_tempscore_0_risklevel9=0
count_vulnibm_iot_tempscore_0_risklevel8=0
count_vulnibm_iot_tempscore_0_risklevel7=0
count_vulnibm_iot_tempscore_0_risklevel6=0
count_vulnibm_iot_tempscore_0_risklevel5=0
count_vulnibm_iot_tempscore_0_risklevel4=0
count_vulnibm_iot_tempscore_0_risklevel3=0
count_vulnibm_iot_tempscore_0_risklevel2=0
count_vulnibm_iot_tempscore_0_risklevel1=0
count_vulnibm_iot_tempscore_0_risklevel0=0





#Recorremos los valores de puntuacion temporal
for r in range(0,len(df_vulnibm_iot["x_xfe_temporal_score"])):                       
    if(df_vulnibm_iot["x_xfe_temporal_score"][r]!='NONE'):
        count_vulnibm_iot_tempscore+=1
        #Comprobamos el valor de puntuacion temporal
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) == 10.0)):
            count_vulnibm_iot_tempscore_10+=1
            #Sumamos el valor de puntuacion de PUNTUACION BASE para un valor de puntuacion temporal especifico
            count_vulnibm_iot_tempscore_10_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_10_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_10_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_10_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_10_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_10_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_10_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_10_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_10_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_10_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_10_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_10_risklevel10+=1
            
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=9.0)):
            
            count_vulnibm_iot_tempscore_9+=1
            count_vulnibm_iot_tempscore_9_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_9_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_9_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_9_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_9_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_9_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_9_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_9_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_9_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_9_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_9_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_9_risklevel10+=1
            
            
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=8.0)):
        
            count_vulnibm_iot_tempscore_8+=1
            count_vulnibm_iot_tempscore_8_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_8_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_8_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_8_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_8_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_8_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_8_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_8_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_8_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_8_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_8_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_8_risklevel10+=1
            
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=7.0)):
        
            count_vulnibm_iot_tempscore_7+=1
            count_vulnibm_iot_tempscore_7_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_7_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_7_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_7_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_7_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_7_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_7_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_7_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_7_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_7_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_7_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_7_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=6.0)):
        
            count_vulnibm_iot_tempscore_6+=1
            count_vulnibm_iot_tempscore_6_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_6_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_6_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_6_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_6_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_6_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_6_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_6_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_6_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_6_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_6_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_6_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=5.0)):
        
            count_vulnibm_iot_tempscore_5+=1
            count_vulnibm_iot_tempscore_5_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_5_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_5_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_5_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_5_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_5_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_5_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_5_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_5_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_5_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_5_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_5_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=4.0)):
            
            count_vulnibm_iot_tempscore_4+=1
            count_vulnibm_iot_tempscore_4_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_4_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_4_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_4_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_4_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_4_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_4_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_4_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_4_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_4_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_4_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_4_risklevel10+=1
            
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=3.0)):
        
        
            count_vulnibm_iot_tempscore_3+=1
            count_vulnibm_iot_tempscore_3_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_3_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_3_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_3_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_3_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_3_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_3_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_3_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_3_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_3_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_3_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_3_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=2.0)):
        
            count_vulnibm_iot_tempscore_2+=1
            count_vulnibm_iot_tempscore_2_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_2_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_2_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_2_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_2_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_2_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_2_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_2_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_2_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_2_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_2_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_2_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=1.0)):
        
            count_vulnibm_iot_tempscore_1+=1
            count_vulnibm_iot_tempscore_1_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_1_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_1_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_1_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_1_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_1_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_1_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_1_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_1_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_1_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_1_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_1_risklevel10+=1
                                         
        if(((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_temporal_score"][r])) >=0.0)):
        
            count_vulnibm_iot_tempscore_0+=1
            count_vulnibm_iot_tempscore_0_risklevel+=float(df_vulnibm_iot["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_iot_tempscore_0_risklevel9+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_iot_tempscore_0_risklevel8+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_iot_tempscore_0_risklevel7+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_iot_tempscore_0_risklevel6+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_iot_tempscore_0_risklevel5+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_iot_tempscore_0_risklevel4+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_iot_tempscore_0_risklevel3+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_iot_tempscore_0_risklevel2+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_iot_tempscore_0_risklevel1+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_iot["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_iot_tempscore_0_risklevel0+=1
            elif(((float(df_vulnibm_iot["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_iot_tempscore_0_risklevel10+=1

                
                

                
                
                
print("***************************ESTADÍSTICAS PUNTUACION TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_tempscore)+" VULNERABILIDADES DONDE EL VALOR DE  PUNTUACION TEMPORAL VIENE ESPECIFICADO :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON  LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_10)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_10_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_10_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_10_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_10_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_10_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_10_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_9)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_9_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_9_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_9_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_9_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_9_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_9_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_8)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 Y 9, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_8_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_8_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_8_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_8_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_8_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_8_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_7)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 Y 8 LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_7_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_7_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_7_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_7_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_7_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_7_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_6)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 Y 7, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_6_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_6_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_6_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_6_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_6_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_6_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_5)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 Y 6, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_5_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_5_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_5_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_5_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_5_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_5_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_4)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 Y 5, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_4_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_4_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_4_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_4_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_4_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_4_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_3)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 Y 4, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_3_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_3_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_3_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_3_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_3_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_3_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_2)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 Y 3, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_2_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_2_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_2_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_2_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_2_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_2_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_1)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 Y 2, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_1_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_1_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_1_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_1_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_1_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_1_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_iot_tempscore_0)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 Y 1, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_0_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_0_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_0_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_0_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_iot_tempscore_0_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_iot_tempscore_0_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")















print("***************************PORCENTAJE PUNTUACION TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_iot_tempscore)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES LOS SIGUIENTES:  \n")
if(count_vulnibm_iot_tempscore_10>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel10*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel9*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel8*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel7*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel6*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel5*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel4*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel3*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel2*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel1*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_10_risklevel0*100)/count_vulnibm_iot_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_10_risklevel)/count_vulnibm_iot_tempscore_10)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_9>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel10*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel9*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel8*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel7*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel6*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel5*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel4*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel3*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel2*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel1*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_9_risklevel0*100)/count_vulnibm_iot_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_9_risklevel)/count_vulnibm_iot_tempscore_9)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_8>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 Y 9 , LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel10*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel9*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel8*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel7*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel6*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel5*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel4*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel3*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel2*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel1*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_8_risklevel0*100)/count_vulnibm_iot_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_8_risklevel)/count_vulnibm_iot_tempscore_8)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_7>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 Y 8, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel10*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel9*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel8*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel7*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel6*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel5*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel4*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel3*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel2*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel1*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_7_risklevel0*100)/count_vulnibm_iot_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_7_risklevel)/count_vulnibm_iot_tempscore_7)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_6>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 Y 7, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel10*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel9*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel8*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel7*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel6*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel5*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel4*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel3*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel2*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel1*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_6_risklevel0*100)/count_vulnibm_iot_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_6_risklevel)/count_vulnibm_iot_tempscore_6)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_5>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 Y 6, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel10*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel9*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel8*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel7*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel6*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel5*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel4*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel3*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel2*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel1*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_5_risklevel0*100)/count_vulnibm_iot_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_5_risklevel)/count_vulnibm_iot_tempscore_5)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_4>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 Y 5, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel10*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel9*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel8*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel7*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel6*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel5*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel4*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel3*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel2*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel1*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_4_risklevel0*100)/count_vulnibm_iot_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_4_risklevel)/count_vulnibm_iot_tempscore_4)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_3>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 Y 4, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel10*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel9*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel8*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel7*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel6*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel5*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel4*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel3*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel2*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel1*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_3_risklevel0*100)/count_vulnibm_iot_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_3_risklevel)/count_vulnibm_iot_tempscore_3)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_2>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 Y 3, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel10*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel9*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel8*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel7*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel6*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel5*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel4*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel3*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel2*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel1*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_2_risklevel0*100)/count_vulnibm_iot_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_2_risklevel)/count_vulnibm_iot_tempscore_2)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_1>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 Y 2, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel10*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel9*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel8*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel7*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel6*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel5*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel4*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel3*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel2*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel1*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_1_risklevel0*100)/count_vulnibm_iot_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_1_risklevel)/count_vulnibm_iot_tempscore_1)))+"\n")
    print("\n")
if(count_vulnibm_iot_tempscore_0>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0*100)/count_vulnibm_iot_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 Y 1, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel10*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel9*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel8*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel7*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel6*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel5*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel4*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel3*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel2*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel1*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_iot_tempscore_0_risklevel0*100)/count_vulnibm_iot_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_iot_tempscore_0_risklevel)/count_vulnibm_iot_tempscore_0)))+"\n")
    print("\n")
    
    
    
    
#Abro los ficheros con los que voy a tratar




df_vulnibm_sh = pd.read_excel('vulnerabilidades_ibm_smart_home_2023.xlsx')



#Variable para almacenar el contador total de valores de puntuacion temporal
count_vulnibm_sh_tempscore=0

#Variables para almacenar el contador total de un valor concreto de puntuacion temporal
count_vulnibm_sh_tempscore_10=0
#Variables para almacenar la suma de valor de PUNTUACION BASE para calcular la media dada una puntuacion temporal especifica
count_vulnibm_sh_tempscore_10_risklevel=0
#Variable para almacenar el contador total de un PUNTUACION BASE dada una puntuacion temporal especifica
count_vulnibm_sh_tempscore_10_risklevel10=0
count_vulnibm_sh_tempscore_10_risklevel9=0
count_vulnibm_sh_tempscore_10_risklevel8=0
count_vulnibm_sh_tempscore_10_risklevel7=0
count_vulnibm_sh_tempscore_10_risklevel6=0
count_vulnibm_sh_tempscore_10_risklevel5=0
count_vulnibm_sh_tempscore_10_risklevel4=0
count_vulnibm_sh_tempscore_10_risklevel3=0
count_vulnibm_sh_tempscore_10_risklevel2=0
count_vulnibm_sh_tempscore_10_risklevel1=0
count_vulnibm_sh_tempscore_10_risklevel0=0



count_vulnibm_sh_tempscore_9=0
count_vulnibm_sh_tempscore_9_risklevel=0
count_vulnibm_sh_tempscore_9_risklevel10=0
count_vulnibm_sh_tempscore_9_risklevel9=0
count_vulnibm_sh_tempscore_9_risklevel8=0
count_vulnibm_sh_tempscore_9_risklevel7=0
count_vulnibm_sh_tempscore_9_risklevel6=0
count_vulnibm_sh_tempscore_9_risklevel5=0
count_vulnibm_sh_tempscore_9_risklevel4=0
count_vulnibm_sh_tempscore_9_risklevel3=0
count_vulnibm_sh_tempscore_9_risklevel2=0
count_vulnibm_sh_tempscore_9_risklevel1=0
count_vulnibm_sh_tempscore_9_risklevel0=0


count_vulnibm_sh_tempscore_8=0
count_vulnibm_sh_tempscore_8_risklevel=0
count_vulnibm_sh_tempscore_8_risklevel10=0
count_vulnibm_sh_tempscore_8_risklevel9=0
count_vulnibm_sh_tempscore_8_risklevel8=0
count_vulnibm_sh_tempscore_8_risklevel7=0
count_vulnibm_sh_tempscore_8_risklevel6=0
count_vulnibm_sh_tempscore_8_risklevel5=0
count_vulnibm_sh_tempscore_8_risklevel4=0
count_vulnibm_sh_tempscore_8_risklevel3=0
count_vulnibm_sh_tempscore_8_risklevel2=0
count_vulnibm_sh_tempscore_8_risklevel1=0
count_vulnibm_sh_tempscore_8_risklevel0=0

count_vulnibm_sh_tempscore_7=0
count_vulnibm_sh_tempscore_7_risklevel=0
count_vulnibm_sh_tempscore_7_risklevel10=0
count_vulnibm_sh_tempscore_7_risklevel9=0
count_vulnibm_sh_tempscore_7_risklevel8=0
count_vulnibm_sh_tempscore_7_risklevel7=0
count_vulnibm_sh_tempscore_7_risklevel6=0
count_vulnibm_sh_tempscore_7_risklevel5=0
count_vulnibm_sh_tempscore_7_risklevel4=0
count_vulnibm_sh_tempscore_7_risklevel3=0
count_vulnibm_sh_tempscore_7_risklevel2=0
count_vulnibm_sh_tempscore_7_risklevel1=0
count_vulnibm_sh_tempscore_7_risklevel0=0


count_vulnibm_sh_tempscore_6=0
count_vulnibm_sh_tempscore_6_risklevel=0
count_vulnibm_sh_tempscore_6_risklevel10=0
count_vulnibm_sh_tempscore_6_risklevel9=0
count_vulnibm_sh_tempscore_6_risklevel8=0
count_vulnibm_sh_tempscore_6_risklevel7=0
count_vulnibm_sh_tempscore_6_risklevel6=0
count_vulnibm_sh_tempscore_6_risklevel5=0
count_vulnibm_sh_tempscore_6_risklevel4=0
count_vulnibm_sh_tempscore_6_risklevel3=0
count_vulnibm_sh_tempscore_6_risklevel2=0
count_vulnibm_sh_tempscore_6_risklevel1=0
count_vulnibm_sh_tempscore_6_risklevel0=0


count_vulnibm_sh_tempscore_5=0
count_vulnibm_sh_tempscore_5_risklevel=0
count_vulnibm_sh_tempscore_5_risklevel10=0
count_vulnibm_sh_tempscore_5_risklevel9=0
count_vulnibm_sh_tempscore_5_risklevel8=0
count_vulnibm_sh_tempscore_5_risklevel7=0
count_vulnibm_sh_tempscore_5_risklevel6=0
count_vulnibm_sh_tempscore_5_risklevel5=0
count_vulnibm_sh_tempscore_5_risklevel4=0
count_vulnibm_sh_tempscore_5_risklevel3=0
count_vulnibm_sh_tempscore_5_risklevel2=0
count_vulnibm_sh_tempscore_5_risklevel1=0
count_vulnibm_sh_tempscore_5_risklevel0=0


count_vulnibm_sh_tempscore_4=0
count_vulnibm_sh_tempscore_4_risklevel=0
count_vulnibm_sh_tempscore_4_risklevel10=0
count_vulnibm_sh_tempscore_4_risklevel9=0
count_vulnibm_sh_tempscore_4_risklevel8=0
count_vulnibm_sh_tempscore_4_risklevel7=0
count_vulnibm_sh_tempscore_4_risklevel6=0
count_vulnibm_sh_tempscore_4_risklevel5=0
count_vulnibm_sh_tempscore_4_risklevel4=0
count_vulnibm_sh_tempscore_4_risklevel3=0
count_vulnibm_sh_tempscore_4_risklevel2=0
count_vulnibm_sh_tempscore_4_risklevel1=0
count_vulnibm_sh_tempscore_4_risklevel0=0

count_vulnibm_sh_tempscore_3=0
count_vulnibm_sh_tempscore_3_risklevel=0
count_vulnibm_sh_tempscore_3_risklevel10=0
count_vulnibm_sh_tempscore_3_risklevel9=0
count_vulnibm_sh_tempscore_3_risklevel8=0
count_vulnibm_sh_tempscore_3_risklevel7=0
count_vulnibm_sh_tempscore_3_risklevel6=0
count_vulnibm_sh_tempscore_3_risklevel5=0
count_vulnibm_sh_tempscore_3_risklevel4=0
count_vulnibm_sh_tempscore_3_risklevel3=0
count_vulnibm_sh_tempscore_3_risklevel2=0
count_vulnibm_sh_tempscore_3_risklevel1=0
count_vulnibm_sh_tempscore_3_risklevel0=0


count_vulnibm_sh_tempscore_2=0
count_vulnibm_sh_tempscore_2_risklevel=0
count_vulnibm_sh_tempscore_2_risklevel10=0
count_vulnibm_sh_tempscore_2_risklevel9=0
count_vulnibm_sh_tempscore_2_risklevel8=0
count_vulnibm_sh_tempscore_2_risklevel7=0
count_vulnibm_sh_tempscore_2_risklevel6=0
count_vulnibm_sh_tempscore_2_risklevel5=0
count_vulnibm_sh_tempscore_2_risklevel4=0
count_vulnibm_sh_tempscore_2_risklevel3=0
count_vulnibm_sh_tempscore_2_risklevel2=0
count_vulnibm_sh_tempscore_2_risklevel1=0
count_vulnibm_sh_tempscore_2_risklevel0=0

count_vulnibm_sh_tempscore_1=0
count_vulnibm_sh_tempscore_1_risklevel=0
count_vulnibm_sh_tempscore_1_risklevel10=0
count_vulnibm_sh_tempscore_1_risklevel9=0
count_vulnibm_sh_tempscore_1_risklevel8=0
count_vulnibm_sh_tempscore_1_risklevel7=0
count_vulnibm_sh_tempscore_1_risklevel6=0
count_vulnibm_sh_tempscore_1_risklevel5=0
count_vulnibm_sh_tempscore_1_risklevel4=0
count_vulnibm_sh_tempscore_1_risklevel3=0
count_vulnibm_sh_tempscore_1_risklevel2=0
count_vulnibm_sh_tempscore_1_risklevel1=0
count_vulnibm_sh_tempscore_1_risklevel0=0

count_vulnibm_sh_tempscore_0=0
count_vulnibm_sh_tempscore_0_risklevel=0
count_vulnibm_sh_tempscore_0_risklevel10=0
count_vulnibm_sh_tempscore_0_risklevel9=0
count_vulnibm_sh_tempscore_0_risklevel8=0
count_vulnibm_sh_tempscore_0_risklevel7=0
count_vulnibm_sh_tempscore_0_risklevel6=0
count_vulnibm_sh_tempscore_0_risklevel5=0
count_vulnibm_sh_tempscore_0_risklevel4=0
count_vulnibm_sh_tempscore_0_risklevel3=0
count_vulnibm_sh_tempscore_0_risklevel2=0
count_vulnibm_sh_tempscore_0_risklevel1=0
count_vulnibm_sh_tempscore_0_risklevel0=0





#Recorremos los valores de puntuacion temporal
for r in range(0,len(df_vulnibm_sh["x_xfe_temporal_score"])):                       
    if(df_vulnibm_sh["x_xfe_temporal_score"][r]!='NONE'):
        count_vulnibm_sh_tempscore+=1
        #Comprobamos el valor de puntuacion temporal
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) == 10.0)):
            count_vulnibm_sh_tempscore_10+=1
            #Sumamos el valor de puntuacion de PUNTUACION BASE para un valor de puntuacion temporal especifico
            count_vulnibm_sh_tempscore_10_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_10_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_10_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_10_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_10_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_10_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_10_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_10_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_10_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_10_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_10_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_10_risklevel10+=1
            
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=9.0)):
            
            count_vulnibm_sh_tempscore_9+=1
            count_vulnibm_sh_tempscore_9_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_9_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_9_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_9_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_9_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_9_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_9_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_9_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_9_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_9_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_9_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_9_risklevel10+=1
            
            
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=8.0)):
        
            count_vulnibm_sh_tempscore_8+=1
            count_vulnibm_sh_tempscore_8_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_8_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_8_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_8_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_8_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_8_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_8_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_8_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_8_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_8_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_8_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_8_risklevel10+=1
            
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=7.0)):
        
            count_vulnibm_sh_tempscore_7+=1
            count_vulnibm_sh_tempscore_7_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_7_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_7_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_7_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_7_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_7_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_7_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_7_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_7_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_7_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_7_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_7_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=6.0)):
        
            count_vulnibm_sh_tempscore_6+=1
            count_vulnibm_sh_tempscore_6_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_6_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_6_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_6_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_6_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_6_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_6_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_6_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_6_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_6_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_6_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_6_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=5.0)):
        
            count_vulnibm_sh_tempscore_5+=1
            count_vulnibm_sh_tempscore_5_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_5_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_5_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_5_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_5_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_5_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_5_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_5_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_5_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_5_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_5_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_5_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=4.0)):
            
            count_vulnibm_sh_tempscore_4+=1
            count_vulnibm_sh_tempscore_4_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_4_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_4_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_4_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_4_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_4_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_4_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_4_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_4_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_4_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_4_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_4_risklevel10+=1
            
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=3.0)):
        
        
            count_vulnibm_sh_tempscore_3+=1
            count_vulnibm_sh_tempscore_3_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_3_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_3_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_3_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_3_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_3_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_3_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_3_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_3_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_3_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_3_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_3_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=2.0)):
        
            count_vulnibm_sh_tempscore_2+=1
            count_vulnibm_sh_tempscore_2_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_2_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_2_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_2_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_2_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_2_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_2_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_2_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_2_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_2_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_2_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_2_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=1.0)):
        
            count_vulnibm_sh_tempscore_1+=1
            count_vulnibm_sh_tempscore_1_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_1_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_1_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_1_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_1_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_1_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_1_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_1_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_1_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_1_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_1_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_1_risklevel10+=1
                                         
        if(((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_temporal_score"][r])) >=0.0)):
        
            count_vulnibm_sh_tempscore_0+=1
            count_vulnibm_sh_tempscore_0_risklevel+=float(df_vulnibm_sh["x_xfe_risk_level"][r])
            if(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 10.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=9.0)):
                count_vulnibm_sh_tempscore_0_risklevel9+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 9.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=8.0)):
                count_vulnibm_sh_tempscore_0_risklevel8+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 8.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=7.0)):
                count_vulnibm_sh_tempscore_0_risklevel7+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 7.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=6.0)):
                count_vulnibm_sh_tempscore_0_risklevel6+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 6.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=5.0)):
                count_vulnibm_sh_tempscore_0_risklevel5+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 5.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=4.0)):
                count_vulnibm_sh_tempscore_0_risklevel4+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 4.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=3.0)):
                count_vulnibm_sh_tempscore_0_risklevel3+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 3.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=2.0)):
                count_vulnibm_sh_tempscore_0_risklevel2+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 2.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=1.0)):
                count_vulnibm_sh_tempscore_0_risklevel1+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) < 1.0) and ((float(df_vulnibm_sh["x_xfe_risk_level"][r])) >=0.0)):
                count_vulnibm_sh_tempscore_0_risklevel0+=1
            elif(((float(df_vulnibm_sh["x_xfe_risk_level"][r])) == 10.0)):
                count_vulnibm_sh_tempscore_0_risklevel10+=1

                
                

                
                
                
print("***************************ESTADÍSTICAS PUNTUACIÓN TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_tempscore)+" VULNERABILIDADES DONDE EL VALOR DE  VIENE ESPECIFICADO :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON  LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_10)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_9)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_8)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 Y 9, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_7)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 Y 8 LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_6)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 Y 7, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_5)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 Y 6, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_4)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 Y 5, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_3)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 Y 4, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_2)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 Y 3, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_1)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 Y 2, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_0)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 Y 1, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")















print("***************************PORCENTAJE PUNTUACION TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE SMART HOME***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_tempscore)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES LOS SIGUIENTES:  \n")
if(count_vulnibm_sh_tempscore_10>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel10*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel9*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel8*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel7*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel6*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel5*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel4*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel3*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel2*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel1*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_10_risklevel0*100)/count_vulnibm_sh_tempscore_10)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel)/count_vulnibm_sh_tempscore_10)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_9>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel10*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel9*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel8*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel7*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel6*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel5*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel4*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel3*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel2*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel1*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_9_risklevel0*100)/count_vulnibm_sh_tempscore_9)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel)/count_vulnibm_sh_tempscore_9)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_8>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 Y 9 , LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel10*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel9*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel8*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel7*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel6*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel5*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel4*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel3*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel2*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel1*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_8_risklevel0*100)/count_vulnibm_sh_tempscore_8)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel)/count_vulnibm_sh_tempscore_8)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_7>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 Y 8, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel10*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel9*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel8*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel7*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel6*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel5*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel4*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel3*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel2*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel1*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_7_risklevel0*100)/count_vulnibm_sh_tempscore_7)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel)/count_vulnibm_sh_tempscore_7)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_6>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 Y 7, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel10*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel9*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel8*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel7*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel6*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel5*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel4*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel3*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel2*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel1*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_6_risklevel0*100)/count_vulnibm_sh_tempscore_6)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel)/count_vulnibm_sh_tempscore_6)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_5>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 Y 6, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel10*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel9*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel8*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel7*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel6*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel5*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel4*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel3*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel2*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel1*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_5_risklevel0*100)/count_vulnibm_sh_tempscore_5)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel)/count_vulnibm_sh_tempscore_5)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_4>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 Y 5, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel10*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel9*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel8*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel7*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel6*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel5*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel4*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel3*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel2*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel1*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_4_risklevel0*100)/count_vulnibm_sh_tempscore_4)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel)/count_vulnibm_sh_tempscore_4)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_3>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 Y 4, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel10*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel9*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel8*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel7*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel6*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel5*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel4*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel3*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel2*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel1*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_3_risklevel0*100)/count_vulnibm_sh_tempscore_3)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel)/count_vulnibm_sh_tempscore_3)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_2>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 Y 3, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel10*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel9*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel8*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel7*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel6*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel5*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel4*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel3*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel2*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel1*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_2_risklevel0*100)/count_vulnibm_sh_tempscore_2)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel)/count_vulnibm_sh_tempscore_2)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_1>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 Y 2, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel10*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel9*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel8*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel7*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel6*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel5*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel4*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel3*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel2*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel1*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_1_risklevel0*100)/count_vulnibm_sh_tempscore_1)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel)/count_vulnibm_sh_tempscore_1)))+"\n")
    print("\n")
if(count_vulnibm_sh_tempscore_0>0):
    print("      -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0*100)/count_vulnibm_sh_tempscore)))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 Y 1, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel10*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel9*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel8*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel7*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel6*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel5*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel4*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel3*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel2*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel1*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float(((count_vulnibm_sh_tempscore_0_risklevel0*100)/count_vulnibm_sh_tempscore_0)))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel)/count_vulnibm_sh_tempscore_0)))+"\n")
    print("\n")
    
    
    
    
    
    
    
    
    
print("***************************ESTADÍSTICAS PUNTUACIÓN TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore)+" VULNERABILIDADES DONDE EL VALOR DE  VIENE ESPECIFICADO :\n") 
print("\n")
print("   - LAS ESTADISTICAS DE VALORES DE PUNTUACION TEMPORAL SON  LAS SIGUIENTES:  \n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel10+count_vulnibm_iot_tempscore_10_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel9+count_vulnibm_iot_tempscore_10_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel8+count_vulnibm_iot_tempscore_10_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel7+count_vulnibm_iot_tempscore_10_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_10_risklevel6+count_vulnibm_iot_tempscore_10_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel5+count_vulnibm_iot_tempscore_10_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel4+count_vulnibm_iot_tempscore_10_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel3+count_vulnibm_iot_tempscore_10_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel2+count_vulnibm_iot_tempscore_10_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel1+count_vulnibm_iot_tempscore_10_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_10_risklevel0+count_vulnibm_iot_tempscore_10_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel10+count_vulnibm_iot_tempscore_9_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel9+count_vulnibm_iot_tempscore_9_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel8+count_vulnibm_iot_tempscore_9_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel7+count_vulnibm_iot_tempscore_9_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_9_risklevel6+count_vulnibm_iot_tempscore_9_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel5+count_vulnibm_iot_tempscore_9_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel4+count_vulnibm_iot_tempscore_9_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel3+count_vulnibm_iot_tempscore_9_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel2+count_vulnibm_iot_tempscore_9_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel1+count_vulnibm_iot_tempscore_9_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_9_risklevel0+count_vulnibm_iot_tempscore_9_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 Y 9, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel10+count_vulnibm_iot_tempscore_8_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel9+count_vulnibm_iot_tempscore_8_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel8+count_vulnibm_iot_tempscore_8_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel7+count_vulnibm_iot_tempscore_8_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_8_risklevel6+count_vulnibm_iot_tempscore_8_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel5+count_vulnibm_iot_tempscore_8_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel4+count_vulnibm_iot_tempscore_8_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel3+count_vulnibm_iot_tempscore_8_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel2+count_vulnibm_iot_tempscore_8_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel1+count_vulnibm_iot_tempscore_8_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_8_risklevel0+count_vulnibm_iot_tempscore_8_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 y 8, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel10+count_vulnibm_iot_tempscore_7_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel9+count_vulnibm_iot_tempscore_7_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel8+count_vulnibm_iot_tempscore_7_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel7+count_vulnibm_iot_tempscore_7_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_7_risklevel6+count_vulnibm_iot_tempscore_7_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel5+count_vulnibm_iot_tempscore_7_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel4+count_vulnibm_iot_tempscore_7_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel3+count_vulnibm_iot_tempscore_7_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel2+count_vulnibm_iot_tempscore_7_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel1+count_vulnibm_iot_tempscore_7_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_7_risklevel0+count_vulnibm_iot_tempscore_7_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 y 7, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel10+count_vulnibm_iot_tempscore_6_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel9+count_vulnibm_iot_tempscore_6_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel8+count_vulnibm_iot_tempscore_6_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel7+count_vulnibm_iot_tempscore_6_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_6_risklevel6+count_vulnibm_iot_tempscore_6_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel5+count_vulnibm_iot_tempscore_6_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel4+count_vulnibm_iot_tempscore_6_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel3+count_vulnibm_iot_tempscore_6_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel2+count_vulnibm_iot_tempscore_6_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel1+count_vulnibm_iot_tempscore_6_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_6_risklevel0+count_vulnibm_iot_tempscore_6_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 y 6, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel10+count_vulnibm_iot_tempscore_5_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel9+count_vulnibm_iot_tempscore_5_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel8+count_vulnibm_iot_tempscore_5_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel7+count_vulnibm_iot_tempscore_5_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_5_risklevel6+count_vulnibm_iot_tempscore_5_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel5+count_vulnibm_iot_tempscore_5_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel4+count_vulnibm_iot_tempscore_5_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel3+count_vulnibm_iot_tempscore_5_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel2+count_vulnibm_iot_tempscore_5_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel1+count_vulnibm_iot_tempscore_5_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_5_risklevel0+count_vulnibm_iot_tempscore_5_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 y 5, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel10+count_vulnibm_iot_tempscore_4_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel9+count_vulnibm_iot_tempscore_4_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel8+count_vulnibm_iot_tempscore_4_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel7+count_vulnibm_iot_tempscore_4_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_4_risklevel6+count_vulnibm_iot_tempscore_4_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel5+count_vulnibm_iot_tempscore_4_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel4+count_vulnibm_iot_tempscore_4_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel3+count_vulnibm_iot_tempscore_4_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel2+count_vulnibm_iot_tempscore_4_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel1+count_vulnibm_iot_tempscore_4_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_4_risklevel0+count_vulnibm_iot_tempscore_4_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 y 4, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel10+count_vulnibm_iot_tempscore_3_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel9+count_vulnibm_iot_tempscore_3_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel8+count_vulnibm_iot_tempscore_3_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel7+count_vulnibm_iot_tempscore_3_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_3_risklevel6+count_vulnibm_iot_tempscore_3_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel5+count_vulnibm_iot_tempscore_3_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel4+count_vulnibm_iot_tempscore_3_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel3+count_vulnibm_iot_tempscore_3_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel2+count_vulnibm_iot_tempscore_3_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel1+count_vulnibm_iot_tempscore_3_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_3_risklevel0+count_vulnibm_iot_tempscore_3_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 y 3, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel10+count_vulnibm_iot_tempscore_2_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel9+count_vulnibm_iot_tempscore_2_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel8+count_vulnibm_iot_tempscore_2_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel7+count_vulnibm_iot_tempscore_2_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_2_risklevel6+count_vulnibm_iot_tempscore_2_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel5+count_vulnibm_iot_tempscore_2_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel4+count_vulnibm_iot_tempscore_2_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel3+count_vulnibm_iot_tempscore_2_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel2+count_vulnibm_iot_tempscore_2_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel1+count_vulnibm_iot_tempscore_2_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_2_risklevel0+count_vulnibm_iot_tempscore_2_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 y 2, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel10+count_vulnibm_iot_tempscore_1_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel9+count_vulnibm_iot_tempscore_1_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel8+count_vulnibm_iot_tempscore_1_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel7+count_vulnibm_iot_tempscore_1_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_1_risklevel6+count_vulnibm_iot_tempscore_1_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel5+count_vulnibm_iot_tempscore_1_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel4+count_vulnibm_iot_tempscore_1_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel3+count_vulnibm_iot_tempscore_1_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel2+count_vulnibm_iot_tempscore_1_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel1+count_vulnibm_iot_tempscore_1_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_1_risklevel0+count_vulnibm_iot_tempscore_1_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")
print("      -    EN  "+str(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0)+" VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 y 1, LAS ESTADÍSTICAS DE PUNTUACION BASE SON LAS SIGUIENTES :  \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel10+count_vulnibm_iot_tempscore_0_risklevel10)+" VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel9+count_vulnibm_iot_tempscore_0_risklevel9)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel8+count_vulnibm_iot_tempscore_0_risklevel8)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel7+count_vulnibm_iot_tempscore_0_risklevel7)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
print("            -    EN  "+str(count_vulnibm_sh_tempscore_0_risklevel6+count_vulnibm_iot_tempscore_0_risklevel6)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel5+count_vulnibm_iot_tempscore_0_risklevel5)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel4+count_vulnibm_iot_tempscore_0_risklevel4)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel3+count_vulnibm_iot_tempscore_0_risklevel3)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel2+count_vulnibm_iot_tempscore_0_risklevel2)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel1+count_vulnibm_iot_tempscore_0_risklevel1)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
print("            -    EN "+str(count_vulnibm_sh_tempscore_0_risklevel0+count_vulnibm_iot_tempscore_0_risklevel0)+" VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
print("\n")







print("***************************PORCENTAJE PUNTUACION TEMPORAL/PUNTUACION BASE VULNERABILIDADES IBM PARTE IOT Y SMART HOME CONJUNTAS***************************")
print("\n")                            
print("\n")
print(" DE UN TOTAL DE "+str(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore)+" VULNERABILIDADES :\n") 
print("\n")
print("   - LOS PORCENTAJES DE VALORES DE PUNTUACION TEMPORAL SON LOS SIGUIENTES LOS SIGUIENTES:  \n")
if((count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ES 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10_risklevel10+count_vulnibm_iot_tempscore_10_risklevel10)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10_risklevel9+count_vulnibm_iot_tempscore_10_risklevel9)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10_risklevel8+count_vulnibm_iot_tempscore_10_risklevel8)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10_risklevel7+count_vulnibm_iot_tempscore_10_risklevel7)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_10_risklevel6+count_vulnibm_iot_tempscore_10_risklevel6)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel5+count_vulnibm_iot_tempscore_10_risklevel5)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel4+count_vulnibm_iot_tempscore_10_risklevel4)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel3+count_vulnibm_iot_tempscore_10_risklevel3)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel2+count_vulnibm_iot_tempscore_10_risklevel2)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel1+count_vulnibm_iot_tempscore_10_risklevel1)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_10_risklevel0+count_vulnibm_iot_tempscore_10_risklevel0)*100)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_10_risklevel+count_vulnibm_iot_tempscore_10_risklevel)/(count_vulnibm_sh_tempscore_10+count_vulnibm_iot_tempscore_10))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 9 Y 10, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9_risklevel10+count_vulnibm_iot_tempscore_9_risklevel10)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9_risklevel9+count_vulnibm_iot_tempscore_9_risklevel9)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9_risklevel8+count_vulnibm_iot_tempscore_9_risklevel8)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9_risklevel7+count_vulnibm_iot_tempscore_9_risklevel7)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_9_risklevel6+count_vulnibm_iot_tempscore_9_risklevel6)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel5+count_vulnibm_iot_tempscore_9_risklevel5)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel4+count_vulnibm_iot_tempscore_9_risklevel4)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel3+count_vulnibm_iot_tempscore_9_risklevel3)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel2+count_vulnibm_iot_tempscore_9_risklevel2)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel1+count_vulnibm_iot_tempscore_9_risklevel1)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_9_risklevel0+count_vulnibm_iot_tempscore_9_risklevel0)*100)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_9_risklevel+count_vulnibm_iot_tempscore_9_risklevel)/(count_vulnibm_sh_tempscore_9+count_vulnibm_iot_tempscore_9))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 8 y 9, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8_risklevel10+count_vulnibm_iot_tempscore_8_risklevel10)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8_risklevel9+count_vulnibm_iot_tempscore_8_risklevel9)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8_risklevel8+count_vulnibm_iot_tempscore_8_risklevel8)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8_risklevel7+count_vulnibm_iot_tempscore_8_risklevel7)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_8_risklevel6+count_vulnibm_iot_tempscore_8_risklevel6)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel5+count_vulnibm_iot_tempscore_8_risklevel5)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel4+count_vulnibm_iot_tempscore_8_risklevel4)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel3+count_vulnibm_iot_tempscore_8_risklevel3)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel2+count_vulnibm_iot_tempscore_8_risklevel2)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel1+count_vulnibm_iot_tempscore_8_risklevel1)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_8_risklevel0+count_vulnibm_iot_tempscore_8_risklevel0)*100)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_8_risklevel+count_vulnibm_iot_tempscore_8_risklevel)/(count_vulnibm_sh_tempscore_8+count_vulnibm_iot_tempscore_8))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 7 y 8, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7_risklevel10+count_vulnibm_iot_tempscore_7_risklevel10)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7_risklevel9+count_vulnibm_iot_tempscore_7_risklevel9)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7_risklevel8+count_vulnibm_iot_tempscore_7_risklevel8)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7_risklevel7+count_vulnibm_iot_tempscore_7_risklevel7)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_7_risklevel6+count_vulnibm_iot_tempscore_7_risklevel6)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel5+count_vulnibm_iot_tempscore_7_risklevel5)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel4+count_vulnibm_iot_tempscore_7_risklevel4)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel3+count_vulnibm_iot_tempscore_7_risklevel3)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel2+count_vulnibm_iot_tempscore_7_risklevel2)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel1+count_vulnibm_iot_tempscore_7_risklevel1)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_7_risklevel0+count_vulnibm_iot_tempscore_7_risklevel0)*100)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_7_risklevel+count_vulnibm_iot_tempscore_7_risklevel)/(count_vulnibm_sh_tempscore_7+count_vulnibm_iot_tempscore_7))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 6 y 7, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6_risklevel10+count_vulnibm_iot_tempscore_6_risklevel10)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6_risklevel9+count_vulnibm_iot_tempscore_6_risklevel9)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6_risklevel8+count_vulnibm_iot_tempscore_6_risklevel8)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6_risklevel7+count_vulnibm_iot_tempscore_6_risklevel7)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_6_risklevel6+count_vulnibm_iot_tempscore_6_risklevel6)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel5+count_vulnibm_iot_tempscore_6_risklevel5)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel4+count_vulnibm_iot_tempscore_6_risklevel4)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel3+count_vulnibm_iot_tempscore_6_risklevel3)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel2+count_vulnibm_iot_tempscore_6_risklevel2)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel1+count_vulnibm_iot_tempscore_6_risklevel1)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_6_risklevel0+count_vulnibm_iot_tempscore_6_risklevel0)*100)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_6_risklevel+count_vulnibm_iot_tempscore_6_risklevel)/(count_vulnibm_sh_tempscore_6+count_vulnibm_iot_tempscore_6))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 5 y 6, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5_risklevel10+count_vulnibm_iot_tempscore_5_risklevel10)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5_risklevel9+count_vulnibm_iot_tempscore_5_risklevel9)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5_risklevel8+count_vulnibm_iot_tempscore_5_risklevel8)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5_risklevel7+count_vulnibm_iot_tempscore_5_risklevel7)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_5_risklevel6+count_vulnibm_iot_tempscore_5_risklevel6)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel5+count_vulnibm_iot_tempscore_5_risklevel5)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel4+count_vulnibm_iot_tempscore_5_risklevel4)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel3+count_vulnibm_iot_tempscore_5_risklevel3)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel2+count_vulnibm_iot_tempscore_5_risklevel2)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel1+count_vulnibm_iot_tempscore_5_risklevel1)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_5_risklevel0+count_vulnibm_iot_tempscore_5_risklevel0)*100)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_5_risklevel+count_vulnibm_iot_tempscore_5_risklevel)/(count_vulnibm_sh_tempscore_5+count_vulnibm_iot_tempscore_5))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 4 y 5, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4_risklevel10+count_vulnibm_iot_tempscore_4_risklevel10)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4_risklevel9+count_vulnibm_iot_tempscore_4_risklevel9)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4_risklevel8+count_vulnibm_iot_tempscore_4_risklevel8)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4_risklevel7+count_vulnibm_iot_tempscore_4_risklevel7)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_4_risklevel6+count_vulnibm_iot_tempscore_4_risklevel6)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel5+count_vulnibm_iot_tempscore_4_risklevel5)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel4+count_vulnibm_iot_tempscore_4_risklevel4)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel3+count_vulnibm_iot_tempscore_4_risklevel3)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel2+count_vulnibm_iot_tempscore_4_risklevel2)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel1+count_vulnibm_iot_tempscore_4_risklevel1)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_4_risklevel0+count_vulnibm_iot_tempscore_4_risklevel0)*100)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_4_risklevel+count_vulnibm_iot_tempscore_4_risklevel)/(count_vulnibm_sh_tempscore_4+count_vulnibm_iot_tempscore_4))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 3 y 4, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3_risklevel10+count_vulnibm_iot_tempscore_3_risklevel10)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3_risklevel9+count_vulnibm_iot_tempscore_3_risklevel9)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3_risklevel8+count_vulnibm_iot_tempscore_3_risklevel8)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3_risklevel7+count_vulnibm_iot_tempscore_3_risklevel7)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_3_risklevel6+count_vulnibm_iot_tempscore_3_risklevel6)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel5+count_vulnibm_iot_tempscore_3_risklevel5)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel4+count_vulnibm_iot_tempscore_3_risklevel4)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel3+count_vulnibm_iot_tempscore_3_risklevel3)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel2+count_vulnibm_iot_tempscore_3_risklevel2)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel1+count_vulnibm_iot_tempscore_3_risklevel1)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_3_risklevel0+count_vulnibm_iot_tempscore_3_risklevel0)*100)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_3_risklevel+count_vulnibm_iot_tempscore_3_risklevel)/(count_vulnibm_sh_tempscore_3+count_vulnibm_iot_tempscore_3))))+"\n")
    print("\n")

if((count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 2 y 3, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2_risklevel10+count_vulnibm_iot_tempscore_2_risklevel10)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2_risklevel9+count_vulnibm_iot_tempscore_2_risklevel9)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2_risklevel8+count_vulnibm_iot_tempscore_2_risklevel8)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2_risklevel7+count_vulnibm_iot_tempscore_2_risklevel7)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_2_risklevel6+count_vulnibm_iot_tempscore_2_risklevel6)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel5+count_vulnibm_iot_tempscore_2_risklevel5)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel4+count_vulnibm_iot_tempscore_2_risklevel4)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel3+count_vulnibm_iot_tempscore_2_risklevel3)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel2+count_vulnibm_iot_tempscore_2_risklevel2)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel1+count_vulnibm_iot_tempscore_2_risklevel1)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_2_risklevel0+count_vulnibm_iot_tempscore_2_risklevel0)*100)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_2_risklevel+count_vulnibm_iot_tempscore_2_risklevel)/(count_vulnibm_sh_tempscore_2+count_vulnibm_iot_tempscore_2))))+"\n")
    print("\n")
if((count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 1 y 2, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1_risklevel10+count_vulnibm_iot_tempscore_1_risklevel10)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1_risklevel9+count_vulnibm_iot_tempscore_1_risklevel9)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1_risklevel8+count_vulnibm_iot_tempscore_1_risklevel8)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1_risklevel7+count_vulnibm_iot_tempscore_1_risklevel7)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_1_risklevel6+count_vulnibm_iot_tempscore_1_risklevel6)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel5+count_vulnibm_iot_tempscore_1_risklevel5)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel4+count_vulnibm_iot_tempscore_1_risklevel4)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel3+count_vulnibm_iot_tempscore_1_risklevel3)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel2+count_vulnibm_iot_tempscore_1_risklevel2)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel1+count_vulnibm_iot_tempscore_1_risklevel1)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_1_risklevel0+count_vulnibm_iot_tempscore_1_risklevel0)*100)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_1_risklevel+count_vulnibm_iot_tempscore_1_risklevel)/(count_vulnibm_sh_tempscore_1+count_vulnibm_iot_tempscore_1))))+"\n")
    print("\n")

if((count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0)>0):
    print("      -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0)*100)/(count_vulnibm_sh_tempscore+count_vulnibm_iot_tempscore))))+" % DE VULNERABILIDADES EL VALOR DE PUNTUACION TEMPORAL ESTÁ ENTRE 0 y 1, LOS PORCENTAJES DE PUNTUACION BASE SON LOS SIGUIENTES :  \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0_risklevel10+count_vulnibm_iot_tempscore_0_risklevel10)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES 10 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0_risklevel9+count_vulnibm_iot_tempscore_0_risklevel9)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 9 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0_risklevel8+count_vulnibm_iot_tempscore_0_risklevel8)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 8 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0_risklevel7+count_vulnibm_iot_tempscore_0_risklevel7)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 7 \n")
    print("            -    EN EL  "+str(float((((count_vulnibm_sh_tempscore_0_risklevel6+count_vulnibm_iot_tempscore_0_risklevel6)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 6 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel5+count_vulnibm_iot_tempscore_0_risklevel5)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 5 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel4+count_vulnibm_iot_tempscore_0_risklevel4)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 4 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel3+count_vulnibm_iot_tempscore_0_risklevel3)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 3 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel2+count_vulnibm_iot_tempscore_0_risklevel2)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 2 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel1+count_vulnibm_iot_tempscore_0_risklevel1)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 1 \n")
    print("            -    EN EL "+str(float((((count_vulnibm_sh_tempscore_0_risklevel0+count_vulnibm_iot_tempscore_0_risklevel0)*100)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+" % DE VULNERABILIDADES EL PUNTUACION BASE ES MAYOR O IGUAL QUE 0 \n")
    print("            -    EL VALOR MEDIO DE PUNTUACION BASE ES  "+str(float(((count_vulnibm_sh_tempscore_0_risklevel+count_vulnibm_iot_tempscore_0_risklevel)/(count_vulnibm_sh_tempscore_0+count_vulnibm_iot_tempscore_0))))+"\n")
    print("\n")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	