



#VECTOR CVSS3 CON PUNTUACION BASE PARTE CVSSV3

import pandas as pd

#Abro los ficheros con los que voy a tratar


df_cve_iot=pd.read_excel('cves_iot_2023.xlsx')
df_cve_sh=pd.read_excel('cves_smart_home_2023.xlsx')


#Variables para almacenar distintos elementos del VECTOR CVSS3 segun la PUNTUACION BASE
cvssV3_BASE_score_10_iot=0

#Variables para almacenar version
cvssV3_BASE_score_10_iot_version_3_0=0
cvssV3_BASE_score_10_iot_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_score_10_iot_attackvector_NETWORK=0
cvssV3_BASE_score_10_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_10_iot_attackvector_LOCAL=0
cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_score_10_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_10_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_10_iot_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_score_10_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_10_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_10_iot_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_score_10_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED=0

#Variables para almacenar el SCOPE
cvssV3_BASE_score_10_iot_scope_CHANGED=0
cvssV3_BASE_score_10_iot_scope_UNCHANGED=0
cvssV3_BASE_score_10_iot_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_10_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_10_iot_confidentialityimpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_score_10_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_10_iot_integrityimpact_LOW=0
cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_10_iot_integrityimpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_score_10_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_10_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_10_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 9

cvssV3_BASE_score_9_iot=0
cvssV3_BASE_score_9_iot_version_3_0=0
cvssV3_BASE_score_9_iot_version_3_1=0

cvssV3_BASE_score_9_iot_attackvector_NETWORK=0
cvssV3_BASE_score_9_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_9_iot_attackvector_LOCAL=0
cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_9_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_9_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_9_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_9_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_9_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_9_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_9_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_9_iot_scope_CHANGED=0
cvssV3_BASE_score_9_iot_scope_UNCHANGED=0
cvssV3_BASE_score_9_iot_scope_NONE=0

cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_9_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_9_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_9_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_9_iot_integrityimpact_LOW=0
cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_9_iot_integrityimpact_NONE=0


cvssV3_BASE_score_9_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_9_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_9_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 8

cvssV3_BASE_score_8_iot=0
cvssV3_BASE_score_8_iot_version_3_0=0
cvssV3_BASE_score_8_iot_version_3_1=0

cvssV3_BASE_score_8_iot_attackvector_NETWORK=0
cvssV3_BASE_score_8_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_8_iot_attackvector_LOCAL=0
cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_8_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_8_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_8_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_8_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_8_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_8_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_8_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_8_iot_scope_CHANGED=0
cvssV3_BASE_score_8_iot_scope_UNCHANGED=0
cvssV3_BASE_score_8_iot_scope_NONE=0

cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_8_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_8_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_8_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_8_iot_integrityimpact_LOW=0
cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_8_iot_integrityimpact_NONE=0


cvssV3_BASE_score_8_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_8_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_8_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 7

cvssV3_BASE_score_7_iot=0
cvssV3_BASE_score_7_iot_version_3_0=0
cvssV3_BASE_score_7_iot_version_3_1=0

cvssV3_BASE_score_7_iot_attackvector_NETWORK=0
cvssV3_BASE_score_7_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_7_iot_attackvector_LOCAL=0
cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_7_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_7_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_7_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_7_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_7_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_7_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_7_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_7_iot_scope_CHANGED=0
cvssV3_BASE_score_7_iot_scope_UNCHANGED=0
cvssV3_BASE_score_7_iot_scope_NONE=0

cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_7_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_7_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_7_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_7_iot_integrityimpact_LOW=0
cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_7_iot_integrityimpact_NONE=0


cvssV3_BASE_score_7_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_7_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_7_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 6

cvssV3_BASE_score_6_iot=0
cvssV3_BASE_score_6_iot_version_3_0=0
cvssV3_BASE_score_6_iot_version_3_1=0

cvssV3_BASE_score_6_iot_attackvector_NETWORK=0
cvssV3_BASE_score_6_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_6_iot_attackvector_LOCAL=0
cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_6_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_6_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_6_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_6_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_6_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_6_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_6_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_6_iot_scope_CHANGED=0
cvssV3_BASE_score_6_iot_scope_UNCHANGED=0
cvssV3_BASE_score_6_iot_scope_NONE=0

cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_6_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_6_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_6_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_6_iot_integrityimpact_LOW=0
cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_6_iot_integrityimpact_NONE=0


cvssV3_BASE_score_6_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_6_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_6_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 5

cvssV3_BASE_score_5_iot=0
cvssV3_BASE_score_5_iot_version_3_0=0
cvssV3_BASE_score_5_iot_version_3_1=0

cvssV3_BASE_score_5_iot_attackvector_NETWORK=0
cvssV3_BASE_score_5_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_5_iot_attackvector_LOCAL=0
cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_5_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_5_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_5_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_5_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_5_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_5_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_5_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_5_iot_scope_CHANGED=0
cvssV3_BASE_score_5_iot_scope_UNCHANGED=0
cvssV3_BASE_score_5_iot_scope_NONE=0

cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_5_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_5_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_5_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_5_iot_integrityimpact_LOW=0
cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_5_iot_integrityimpact_NONE=0


cvssV3_BASE_score_5_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_5_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_5_iot_availabilityimpact_NONE=0



# PUNTUACION BASE 4

cvssV3_BASE_score_4_iot=0
cvssV3_BASE_score_4_iot_version_3_0=0
cvssV3_BASE_score_4_iot_version_3_1=0

cvssV3_BASE_score_4_iot_attackvector_NETWORK=0
cvssV3_BASE_score_4_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_4_iot_attackvector_LOCAL=0
cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_4_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_4_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_4_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_4_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_4_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_4_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_4_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_4_iot_scope_CHANGED=0
cvssV3_BASE_score_4_iot_scope_UNCHANGED=0
cvssV3_BASE_score_4_iot_scope_NONE=0

cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_4_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_4_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_4_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_4_iot_integrityimpact_LOW=0
cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_4_iot_integrityimpact_NONE=0


cvssV3_BASE_score_4_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_4_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_4_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 3

cvssV3_BASE_score_3_iot=0
cvssV3_BASE_score_3_iot_version_3_0=0
cvssV3_BASE_score_3_iot_version_3_1=0

cvssV3_BASE_score_3_iot_attackvector_NETWORK=0
cvssV3_BASE_score_3_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_3_iot_attackvector_LOCAL=0
cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_3_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_3_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_3_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_3_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_3_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_3_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_3_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_3_iot_scope_CHANGED=0
cvssV3_BASE_score_3_iot_scope_UNCHANGED=0
cvssV3_BASE_score_3_iot_scope_NONE=0

cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_3_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_3_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_3_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_3_iot_integrityimpact_LOW=0
cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_3_iot_integrityimpact_NONE=0


cvssV3_BASE_score_3_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_3_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_3_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 2

cvssV3_BASE_score_2_iot=0
cvssV3_BASE_score_2_iot_version_3_0=0
cvssV3_BASE_score_2_iot_version_3_1=0

cvssV3_BASE_score_2_iot_attackvector_NETWORK=0
cvssV3_BASE_score_2_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_2_iot_attackvector_LOCAL=0
cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_2_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_2_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_2_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_2_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_2_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_2_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_2_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_2_iot_scope_CHANGED=0
cvssV3_BASE_score_2_iot_scope_UNCHANGED=0
cvssV3_BASE_score_2_iot_scope_NONE=0

cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_2_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_2_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_2_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_2_iot_integrityimpact_LOW=0
cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_2_iot_integrityimpact_NONE=0


cvssV3_BASE_score_2_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_2_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_2_iot_availabilityimpact_NONE=0

# PUNTUACION BASE 1
cvssV3_BASE_score_1_iot=0
cvssV3_BASE_score_1_iot_version_3_0=0
cvssV3_BASE_score_1_iot_version_3_1=0

cvssV3_BASE_score_1_iot_attackvector_NETWORK=0
cvssV3_BASE_score_1_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_1_iot_attackvector_LOCAL=0
cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_1_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_1_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_1_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_1_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_1_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_1_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_1_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_1_iot_scope_CHANGED=0
cvssV3_BASE_score_1_iot_scope_UNCHANGED=0
cvssV3_BASE_score_1_iot_scope_NONE=0

cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_1_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_1_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_1_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_1_iot_integrityimpact_LOW=0
cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_1_iot_integrityimpact_NONE=0


cvssV3_BASE_score_1_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_1_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_1_iot_availabilityimpact_NONE=0


# PUNTUACION BASE 0
cvssV3_BASE_score_0_iot=0
cvssV3_BASE_score_0_iot_version_3_0=0
cvssV3_BASE_score_0_iot_version_3_1=0

cvssV3_BASE_score_0_iot_attackvector_NETWORK=0
cvssV3_BASE_score_0_iot_attackvector_PHYSICAL=0
cvssV3_BASE_score_0_iot_attackvector_LOCAL=0
cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_0_iot_attackcomplexity_HIGH=0
cvssV3_BASE_score_0_iot_attackcomplexity_LOW=0
cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_0_iot_attackcomplexity_NONE=0

cvssV3_BASE_score_0_iot_privilegesrequired_HIGH=0
cvssV3_BASE_score_0_iot_privilegesrequired_LOW=0
cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_0_iot_privilegesrequired_NONE=0

cvssV3_BASE_score_0_iot_userinteraction_REQUIRED=0
cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_0_iot_scope_CHANGED=0
cvssV3_BASE_score_0_iot_scope_UNCHANGED=0
cvssV3_BASE_score_0_iot_scope_NONE=0

cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH=0
cvssV3_BASE_score_0_iot_confidentialityimpact_LOW=0
cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_0_iot_confidentialityimpact_NONE=0


cvssV3_BASE_score_0_iot_integrityimpact_HIGH=0
cvssV3_BASE_score_0_iot_integrityimpact_LOW=0
cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM=0
cvssV3_BASE_score_0_iot_integrityimpact_NONE=0


cvssV3_BASE_score_0_iot_availabilityimpact_HIGH=0
cvssV3_BASE_score_0_iot_availabilityimpact_LOW=0
cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_0_iot_availabilityimpact_NONE=0


# NO PUNTUACION BASE
cvssV3_no_BASE_score_iot=0
cvssV3_no_BASE_score_iot_version_3_0=0
cvssV3_no_BASE_score_iot_version_3_1=0

cvssV3_no_BASE_score_iot_attackvector_NETWORK=0
cvssV3_no_BASE_score_iot_attackvector_PHYSICAL=0
cvssV3_no_BASE_score_iot_attackvector_LOCAL=0
cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK=0

cvssV3_no_BASE_score_iot_attackcomplexity_HIGH=0
cvssV3_no_BASE_score_iot_attackcomplexity_LOW=0
cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM=0
cvssV3_no_BASE_score_iot_attackcomplexity_NONE=0

cvssV3_no_BASE_score_iot_privilegesrequired_HIGH=0
cvssV3_no_BASE_score_iot_privilegesrequired_LOW=0
cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM=0
cvssV3_no_BASE_score_iot_privilegesrequired_NONE=0

cvssV3_no_BASE_score_iot_userinteraction_REQUIRED=0
cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED=0

cvssV3_no_BASE_score_iot_scope_CHANGED=0
cvssV3_no_BASE_score_iot_scope_UNCHANGED=0
cvssV3_no_BASE_score_iot_scope_NONE=0

cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH=0
cvssV3_no_BASE_score_iot_confidentialityimpact_LOW=0
cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM=0
cvssV3_no_BASE_score_iot_confidentialityimpact_NONE=0


cvssV3_no_BASE_score_iot_integrityimpact_HIGH=0
cvssV3_no_BASE_score_iot_integrityimpact_LOW=0
cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM=0
cvssV3_no_BASE_score_iot_integrityimpact_NONE=0


cvssV3_no_BASE_score_iot_availabilityimpact_HIGH=0
cvssV3_no_BASE_score_iot_availabilityimpact_LOW=0
cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM=0
cvssV3_no_BASE_score_iot_availabilityimpact_NONE=0

#Compruebo la puntuacion base CVE CVSS3 para IOT

for j in range(0,len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])):
    if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j] =='NONE'):
        cvssV3_no_BASE_score_iot+=1
        #Compruebo la version del vector
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_no_BASE_score_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_no_BASE_score_iot_version_3_0+=1
        #Compruebo el vector de ataque  
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_no_BASE_score_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_no_BASE_score_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_no_BASE_score_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK+=1
        #Compruebo la complejidad de ataque   
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_no_BASE_score_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_no_BASE_score_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_iot_attackcomplexity_NONE+=1  
        #Compruebo los privilegios requeridos  
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_no_BASE_score_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_no_BASE_score_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_iot_privilegesrequired_NONE+=1
            
        #Compruebo si se requiere la interaccion del usuario  
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_no_BASE_score_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED+=1
            
        #Compruebo el scope
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_no_BASE_score_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_no_BASE_score_iot_scope_UNCHANGED+=1
        else:
            cvssV3_no_BASE_score_iot_scope_NONE+=1
            
        #Compruebo el impacto de confidencialidad   
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_iot_confidentialityimpact_NONE+=1 
            
        #Compruebo el impacto de integridad   
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_iot_integrityimpact_NONE+=1    
            
        #Compruebo el impacto de disponibilidad  
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_iot_availabilityimpact_NONE+=1
    
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 10.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=9.0)):
        cvssV3_BASE_score_9_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_9_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_9_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_9_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_9_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_9_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_9_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_9_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_9_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_9_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_9_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_9_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_9_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_9_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_iot_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 9.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=8.0)):
        cvssV3_BASE_score_8_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_8_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_8_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_8_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_8_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_8_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_8_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_8_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_8_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_8_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_8_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_8_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_8_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_8_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_iot_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 8.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=7.0)):
        cvssV3_BASE_score_7_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_7_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_7_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_7_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_7_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_7_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_7_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_7_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_7_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_7_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_7_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_7_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_7_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_7_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_iot_availabilityimpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 7.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=6.0)):
        cvssV3_BASE_score_6_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_6_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_6_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_6_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_6_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_6_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_6_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_6_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_6_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_6_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_6_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_6_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_6_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_6_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_iot_availabilityimpact_NONE+=1

            
            
            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 6.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=5.0)):
        cvssV3_BASE_score_5_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_5_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_5_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_5_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_5_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_5_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_5_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_5_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_5_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_5_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_5_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_5_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_5_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_5_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_iot_availabilityimpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 5.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=4.0)):
        cvssV3_BASE_score_4_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_4_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_4_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_4_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_4_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_4_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_4_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_4_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_4_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_4_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_4_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_4_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_4_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_4_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_iot_availabilityimpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 4.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=3.0)):
        cvssV3_BASE_score_3_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_3_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_3_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_3_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_3_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_3_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_3_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_3_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_3_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_3_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_3_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_3_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_3_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_3_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_iot_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 3.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=2.0)):
        cvssV3_BASE_score_2_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_2_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_2_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_2_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_2_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_2_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_2_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_2_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_2_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_2_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_2_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_2_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_2_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_2_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_iot_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 2.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=1.0)):
        cvssV3_BASE_score_1_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_1_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_1_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_1_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_1_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_1_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_1_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_1_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_1_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_1_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_1_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_1_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_1_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_1_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_iot_availabilityimpact_NONE+=1

            
            
            
    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 1.0) and ((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=0.0)):
        cvssV3_BASE_score_0_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_0_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_0_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_0_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_0_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_0_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_0_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_0_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_0_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_0_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_0_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_0_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_0_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_0_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_iot_availabilityimpact_NONE+=1

    elif(((float(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) == 10.0)):
        cvssV3_BASE_score_10_iot+=1
        
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_10_iot_version_3_1+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_10_iot_version_3_0+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_10_iot_attackvector_NETWORK+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_10_iot_attackvector_LOCAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_10_iot_attackvector_PHYSICAL+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_10_iot_attackcomplexity_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_10_iot_attackcomplexity_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_iot_attackcomplexity_NONE+=1  
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_10_iot_privilegesrequired_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_10_iot_privilegesrequired_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_iot_privilegesrequired_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_10_iot_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_10_iot_scope_CHANGED+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_10_iot_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_10_iot_scope_NONE+=1
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_iot_confidentialityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_iot_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_iot_integrityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_iot_integrityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_iot_integrityimpact_NONE+=1    
            
          
        if(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_iot_availabilityimpact_HIGH+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_iot_availabilityimpact_LOW+=1
        elif(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_iot_availabilityimpact_NONE+=1

            
            
            
print("________________________ESTADÍSTICAS ELEMENTOS VECTOR CVSS3 SEGÚN PUNTUACION BASE CVSSV3 PARTE IOT________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE LA RELACION DE ELEMENTOS DEL VECTOR CVSS3 SEGUN PUNTUACION BASE SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_10_iot)+" VULNERABILIDADES LA PUNTUACION BASE ES 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_9_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_8_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_7_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_6_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 Y 7. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_5_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 Y 6. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_4_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 Y 5. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_3_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 Y 4. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_2_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 Y 3. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_1_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 Y 2. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_0_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 Y 1. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")

print("      -    EN  "+str(cvssV3_no_BASE_score_iot)+" VULNERABILIDADES LA PUNTUACIÓN BASE NO ESTÁ DEFINIDA. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")            
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
          
            
            
        
            
print("________________________PORCENTAJES ELEMENTOS VECTOR CVSS3-PUNTUACION BASE CVSSV3 PARTE IOT________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+" VULNERABILIDADES ,  LOS PORCENTAJES DE LA RELACION DE ELEMENTOS DEL VECTOR CVSS3 SEGUN PUNTUACION BASE SON LOS SIGUIENTES:   \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_10_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ES 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_version_3_1*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_version_3_0*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_scope_CHANGED*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_scope_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_10_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")            
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_9_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_version_3_1*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_version_3_0*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_scope_CHANGED*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_scope_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_9_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_8_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_version_3_1*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_version_3_0*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_scope_CHANGED*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_scope_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_8_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_7_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_version_3_1*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_version_3_0*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_scope_CHANGED*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_scope_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_7_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_6_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 Y 7. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_version_3_1*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_version_3_0*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_scope_CHANGED*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_scope_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_6_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_5_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 Y 6. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_version_3_1*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_version_3_0*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_scope_CHANGED*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_scope_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_5_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_4_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 Y 5. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_version_3_1*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_version_3_0*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_scope_CHANGED*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_scope_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_4_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_3_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 Y 4. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_version_3_1*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_version_3_0*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_scope_CHANGED*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_scope_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_3_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
if(cvssV3_BASE_score_2_iot>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_2_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 Y 3. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_version_3_1*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_version_3_0*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_scope_CHANGED*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_scope_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_2_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")  
if(cvssV3_BASE_score_1_iot>0):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_1_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 Y 2. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_version_3_1*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_version_3_0*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_scope_CHANGED*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_scope_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_1_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")   
if(cvssV3_BASE_score_0_iot):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_0_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 Y 1. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_version_3_1*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_version_3_0*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackvector_NETWORK*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackvector_LOCAL*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackvector_PHYSICAL*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackcomplexity_HIGH*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackcomplexity_LOW*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_attackcomplexity_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_privilegesrequired_HIGH*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_privilegesrequired_LOW*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_privilegesrequired_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_userinteraction_REQUIRED*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_scope_CHANGED*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_scope_UNCHANGED*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_scope_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_confidentialityimpact_LOW*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_confidentialityimpact_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_integrityimpact_HIGH*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_integrityimpact_LOW*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_integrityimpact_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_availabilityimpact_HIGH*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_availabilityimpact_LOW*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_iot_availabilityimpact_NONE*100)/cvssV3_BASE_score_0_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_no_BASE_score_iot*100)/len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE NO VIENE ESPECIFICADA. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_version_3_1*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_version_3_0*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackvector_NETWORK*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackvector_LOCAL*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackvector_PHYSICAL*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackcomplexity_HIGH*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackcomplexity_LOW*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_attackcomplexity_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_privilegesrequired_HIGH*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_privilegesrequired_LOW*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_privilegesrequired_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_userinteraction_REQUIRED*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_scope_CHANGED*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_scope_UNCHANGED*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_scope_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_confidentialityimpact_LOW*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_confidentialityimpact_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_integrityimpact_HIGH*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_integrityimpact_LOW*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_integrityimpact_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_availabilityimpact_HIGH*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_availabilityimpact_LOW*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_iot_availabilityimpact_NONE*100)/cvssV3_no_BASE_score_iot)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
            
            
        
            
       

    
    
    


#Variables para almacenar distintos elementos del VECTOR CVSS3 segun la PUNTUACION BASE
cvssV3_BASE_score_10_sh=0

#Variables para almacenar version
cvssV3_BASE_score_10_sh_version_3_0=0
cvssV3_BASE_score_10_sh_version_3_1=0

#Variables para almacenar vector de ataque
cvssV3_BASE_score_10_sh_attackvector_NETWORK=0
cvssV3_BASE_score_10_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_10_sh_attackvector_LOCAL=0
cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK=0

#Variables para almacenar complejidad de ataque
cvssV3_BASE_score_10_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_10_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_10_sh_attackcomplexity_NONE=0

#Variables para almacenar privilegios requeridos
cvssV3_BASE_score_10_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_10_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_10_sh_privilegesrequired_NONE=0

#Variables para almacenar si se requiere la interaccion del usuario
cvssV3_BASE_score_10_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED=0

#Variables para almacenar el SCOPE
cvssV3_BASE_score_10_sh_scope_CHANGED=0
cvssV3_BASE_score_10_sh_scope_UNCHANGED=0
cvssV3_BASE_score_10_sh_scope_NONE=0

#Variables para almacenar el impacto de confidencialidad
cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_10_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_10_sh_confidentialityimpact_NONE=0

#Variables para almacenar el impacto de integridad
cvssV3_BASE_score_10_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_10_sh_integrityimpact_LOW=0
cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_10_sh_integrityimpact_NONE=0

#Variables para almacenar el impacto de disponibilidad
cvssV3_BASE_score_10_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_10_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_10_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 9

cvssV3_BASE_score_9_sh=0
cvssV3_BASE_score_9_sh_version_3_0=0
cvssV3_BASE_score_9_sh_version_3_1=0

cvssV3_BASE_score_9_sh_attackvector_NETWORK=0
cvssV3_BASE_score_9_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_9_sh_attackvector_LOCAL=0
cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_9_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_9_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_9_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_9_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_9_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_9_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_9_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_9_sh_scope_CHANGED=0
cvssV3_BASE_score_9_sh_scope_UNCHANGED=0
cvssV3_BASE_score_9_sh_scope_NONE=0

cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_9_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_9_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_9_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_9_sh_integrityimpact_LOW=0
cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_9_sh_integrityimpact_NONE=0


cvssV3_BASE_score_9_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_9_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_9_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 8

cvssV3_BASE_score_8_sh=0
cvssV3_BASE_score_8_sh_version_3_0=0
cvssV3_BASE_score_8_sh_version_3_1=0

cvssV3_BASE_score_8_sh_attackvector_NETWORK=0
cvssV3_BASE_score_8_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_8_sh_attackvector_LOCAL=0
cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_8_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_8_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_8_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_8_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_8_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_8_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_8_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_8_sh_scope_CHANGED=0
cvssV3_BASE_score_8_sh_scope_UNCHANGED=0
cvssV3_BASE_score_8_sh_scope_NONE=0

cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_8_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_8_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_8_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_8_sh_integrityimpact_LOW=0
cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_8_sh_integrityimpact_NONE=0


cvssV3_BASE_score_8_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_8_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_8_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 7

cvssV3_BASE_score_7_sh=0
cvssV3_BASE_score_7_sh_version_3_0=0
cvssV3_BASE_score_7_sh_version_3_1=0

cvssV3_BASE_score_7_sh_attackvector_NETWORK=0
cvssV3_BASE_score_7_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_7_sh_attackvector_LOCAL=0
cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_7_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_7_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_7_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_7_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_7_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_7_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_7_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_7_sh_scope_CHANGED=0
cvssV3_BASE_score_7_sh_scope_UNCHANGED=0
cvssV3_BASE_score_7_sh_scope_NONE=0

cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_7_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_7_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_7_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_7_sh_integrityimpact_LOW=0
cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_7_sh_integrityimpact_NONE=0


cvssV3_BASE_score_7_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_7_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_7_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 6

cvssV3_BASE_score_6_sh=0
cvssV3_BASE_score_6_sh_version_3_0=0
cvssV3_BASE_score_6_sh_version_3_1=0

cvssV3_BASE_score_6_sh_attackvector_NETWORK=0
cvssV3_BASE_score_6_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_6_sh_attackvector_LOCAL=0
cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_6_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_6_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_6_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_6_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_6_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_6_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_6_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_6_sh_scope_CHANGED=0
cvssV3_BASE_score_6_sh_scope_UNCHANGED=0
cvssV3_BASE_score_6_sh_scope_NONE=0

cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_6_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_6_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_6_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_6_sh_integrityimpact_LOW=0
cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_6_sh_integrityimpact_NONE=0


cvssV3_BASE_score_6_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_6_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_6_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 5

cvssV3_BASE_score_5_sh=0
cvssV3_BASE_score_5_sh_version_3_0=0
cvssV3_BASE_score_5_sh_version_3_1=0

cvssV3_BASE_score_5_sh_attackvector_NETWORK=0
cvssV3_BASE_score_5_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_5_sh_attackvector_LOCAL=0
cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_5_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_5_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_5_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_5_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_5_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_5_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_5_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_5_sh_scope_CHANGED=0
cvssV3_BASE_score_5_sh_scope_UNCHANGED=0
cvssV3_BASE_score_5_sh_scope_NONE=0

cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_5_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_5_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_5_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_5_sh_integrityimpact_LOW=0
cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_5_sh_integrityimpact_NONE=0


cvssV3_BASE_score_5_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_5_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_5_sh_availabilityimpact_NONE=0



# PUNTUACION BASE 4

cvssV3_BASE_score_4_sh=0
cvssV3_BASE_score_4_sh_version_3_0=0
cvssV3_BASE_score_4_sh_version_3_1=0

cvssV3_BASE_score_4_sh_attackvector_NETWORK=0
cvssV3_BASE_score_4_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_4_sh_attackvector_LOCAL=0
cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_4_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_4_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_4_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_4_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_4_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_4_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_4_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_4_sh_scope_CHANGED=0
cvssV3_BASE_score_4_sh_scope_UNCHANGED=0
cvssV3_BASE_score_4_sh_scope_NONE=0

cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_4_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_4_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_4_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_4_sh_integrityimpact_LOW=0
cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_4_sh_integrityimpact_NONE=0


cvssV3_BASE_score_4_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_4_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_4_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 3

cvssV3_BASE_score_3_sh=0
cvssV3_BASE_score_3_sh_version_3_0=0
cvssV3_BASE_score_3_sh_version_3_1=0

cvssV3_BASE_score_3_sh_attackvector_NETWORK=0
cvssV3_BASE_score_3_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_3_sh_attackvector_LOCAL=0
cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_3_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_3_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_3_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_3_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_3_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_3_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_3_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_3_sh_scope_CHANGED=0
cvssV3_BASE_score_3_sh_scope_UNCHANGED=0
cvssV3_BASE_score_3_sh_scope_NONE=0

cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_3_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_3_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_3_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_3_sh_integrityimpact_LOW=0
cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_3_sh_integrityimpact_NONE=0


cvssV3_BASE_score_3_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_3_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_3_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 2

cvssV3_BASE_score_2_sh=0
cvssV3_BASE_score_2_sh_version_3_0=0
cvssV3_BASE_score_2_sh_version_3_1=0

cvssV3_BASE_score_2_sh_attackvector_NETWORK=0
cvssV3_BASE_score_2_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_2_sh_attackvector_LOCAL=0
cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_2_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_2_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_2_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_2_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_2_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_2_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_2_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_2_sh_scope_CHANGED=0
cvssV3_BASE_score_2_sh_scope_UNCHANGED=0
cvssV3_BASE_score_2_sh_scope_NONE=0

cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_2_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_2_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_2_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_2_sh_integrityimpact_LOW=0
cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_2_sh_integrityimpact_NONE=0


cvssV3_BASE_score_2_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_2_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_2_sh_availabilityimpact_NONE=0

# PUNTUACION BASE 1
cvssV3_BASE_score_1_sh=0
cvssV3_BASE_score_1_sh_version_3_0=0
cvssV3_BASE_score_1_sh_version_3_1=0

cvssV3_BASE_score_1_sh_attackvector_NETWORK=0
cvssV3_BASE_score_1_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_1_sh_attackvector_LOCAL=0
cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_1_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_1_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_1_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_1_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_1_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_1_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_1_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_1_sh_scope_CHANGED=0
cvssV3_BASE_score_1_sh_scope_UNCHANGED=0
cvssV3_BASE_score_1_sh_scope_NONE=0

cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_1_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_1_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_1_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_1_sh_integrityimpact_LOW=0
cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_1_sh_integrityimpact_NONE=0


cvssV3_BASE_score_1_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_1_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_1_sh_availabilityimpact_NONE=0


# PUNTUACION BASE 0
cvssV3_BASE_score_0_sh=0
cvssV3_BASE_score_0_sh_version_3_0=0
cvssV3_BASE_score_0_sh_version_3_1=0

cvssV3_BASE_score_0_sh_attackvector_NETWORK=0
cvssV3_BASE_score_0_sh_attackvector_PHYSICAL=0
cvssV3_BASE_score_0_sh_attackvector_LOCAL=0
cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_BASE_score_0_sh_attackcomplexity_HIGH=0
cvssV3_BASE_score_0_sh_attackcomplexity_LOW=0
cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM=0
cvssV3_BASE_score_0_sh_attackcomplexity_NONE=0

cvssV3_BASE_score_0_sh_privilegesrequired_HIGH=0
cvssV3_BASE_score_0_sh_privilegesrequired_LOW=0
cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM=0
cvssV3_BASE_score_0_sh_privilegesrequired_NONE=0

cvssV3_BASE_score_0_sh_userinteraction_REQUIRED=0
cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED=0

cvssV3_BASE_score_0_sh_scope_CHANGED=0
cvssV3_BASE_score_0_sh_scope_UNCHANGED=0
cvssV3_BASE_score_0_sh_scope_NONE=0

cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH=0
cvssV3_BASE_score_0_sh_confidentialityimpact_LOW=0
cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM=0
cvssV3_BASE_score_0_sh_confidentialityimpact_NONE=0


cvssV3_BASE_score_0_sh_integrityimpact_HIGH=0
cvssV3_BASE_score_0_sh_integrityimpact_LOW=0
cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM=0
cvssV3_BASE_score_0_sh_integrityimpact_NONE=0


cvssV3_BASE_score_0_sh_availabilityimpact_HIGH=0
cvssV3_BASE_score_0_sh_availabilityimpact_LOW=0
cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM=0
cvssV3_BASE_score_0_sh_availabilityimpact_NONE=0


# NO PUNTUACION BASE
cvssV3_no_BASE_score_sh=0
cvssV3_no_BASE_score_sh_version_3_0=0
cvssV3_no_BASE_score_sh_version_3_1=0

cvssV3_no_BASE_score_sh_attackvector_NETWORK=0
cvssV3_no_BASE_score_sh_attackvector_PHYSICAL=0
cvssV3_no_BASE_score_sh_attackvector_LOCAL=0
cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK=0

cvssV3_no_BASE_score_sh_attackcomplexity_HIGH=0
cvssV3_no_BASE_score_sh_attackcomplexity_LOW=0
cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM=0
cvssV3_no_BASE_score_sh_attackcomplexity_NONE=0

cvssV3_no_BASE_score_sh_privilegesrequired_HIGH=0
cvssV3_no_BASE_score_sh_privilegesrequired_LOW=0
cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM=0
cvssV3_no_BASE_score_sh_privilegesrequired_NONE=0

cvssV3_no_BASE_score_sh_userinteraction_REQUIRED=0
cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED=0

cvssV3_no_BASE_score_sh_scope_CHANGED=0
cvssV3_no_BASE_score_sh_scope_UNCHANGED=0
cvssV3_no_BASE_score_sh_scope_NONE=0

cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH=0
cvssV3_no_BASE_score_sh_confidentialityimpact_LOW=0
cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM=0
cvssV3_no_BASE_score_sh_confidentialityimpact_NONE=0


cvssV3_no_BASE_score_sh_integrityimpact_HIGH=0
cvssV3_no_BASE_score_sh_integrityimpact_LOW=0
cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM=0
cvssV3_no_BASE_score_sh_integrityimpact_NONE=0


cvssV3_no_BASE_score_sh_availabilityimpact_HIGH=0
cvssV3_no_BASE_score_sh_availabilityimpact_LOW=0
cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM=0
cvssV3_no_BASE_score_sh_availabilityimpact_NONE=0

#Compruebo la puntuacion base CVE CVSS3 para SMART HOME

for j in range(0,len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])):
    if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j] =='NONE'):
        cvssV3_no_BASE_score_sh+=1
        #Compruebo la version del vector
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_no_BASE_score_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_no_BASE_score_sh_version_3_0+=1
        #Compruebo el vector de ataque  
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_no_BASE_score_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_no_BASE_score_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_no_BASE_score_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK+=1
        #Compruebo la complejidad de ataque   
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_no_BASE_score_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_no_BASE_score_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_sh_attackcomplexity_NONE+=1  
        #Compruebo los privilegios requeridos  
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_no_BASE_score_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_no_BASE_score_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_sh_privilegesrequired_NONE+=1
            
        #Compruebo si se requiere la interaccion del usuario  
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_no_BASE_score_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED+=1
            
        #Compruebo el scope
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_no_BASE_score_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_no_BASE_score_sh_scope_UNCHANGED+=1
        else:
            cvssV3_no_BASE_score_sh_scope_NONE+=1
            
        #Compruebo el impacto de confidencialidad   
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_sh_confidentialityimpact_NONE+=1 
            
        #Compruebo el impacto de integridad   
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_sh_integrityimpact_NONE+=1    
            
        #Compruebo el impacto de disponibilidad  
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_no_BASE_score_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_no_BASE_score_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_no_BASE_score_sh_availabilityimpact_NONE+=1
    
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 10.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=9.0)):
        cvssV3_BASE_score_9_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_9_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_9_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_9_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_9_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_9_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_9_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_9_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_9_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_9_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_9_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_9_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_9_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_9_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_9_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_9_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_9_sh_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 9.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=8.0)):
        cvssV3_BASE_score_8_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_8_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_8_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_8_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_8_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_8_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_8_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_8_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_8_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_8_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_8_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_8_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_8_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_8_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_8_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_8_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_8_sh_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 8.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=7.0)):
        cvssV3_BASE_score_7_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_7_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_7_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_7_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_7_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_7_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_7_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_7_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_7_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_7_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_7_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_7_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_7_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_7_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_7_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_7_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_7_sh_availabilityimpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 7.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=6.0)):
        cvssV3_BASE_score_6_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_6_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_6_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_6_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_6_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_6_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_6_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_6_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_6_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_6_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_6_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_6_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_6_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_6_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_6_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_6_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_6_sh_availabilityimpact_NONE+=1

            
            
            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 6.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=5.0)):
        cvssV3_BASE_score_5_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_5_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_5_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_5_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_5_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_5_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_5_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_5_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_5_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_5_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_5_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_5_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_5_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_5_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_5_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_5_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_5_sh_availabilityimpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 5.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=4.0)):
        cvssV3_BASE_score_4_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_4_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_4_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_4_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_4_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_4_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_4_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_4_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_4_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_4_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_4_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_4_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_4_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_4_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_4_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_4_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_4_sh_availabilityimpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 4.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=3.0)):
        cvssV3_BASE_score_3_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_3_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_3_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_3_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_3_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_3_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_3_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_3_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_3_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_3_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_3_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_3_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_3_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_3_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_3_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_3_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_3_sh_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 3.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=2.0)):
        cvssV3_BASE_score_2_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_2_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_2_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_2_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_2_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_2_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_2_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_2_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_2_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_2_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_2_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_2_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_2_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_2_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_2_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_2_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_2_sh_availabilityimpact_NONE+=1

            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 2.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=1.0)):
        cvssV3_BASE_score_1_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_1_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_1_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_1_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_1_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_1_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_1_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_1_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_1_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_1_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_1_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_1_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_1_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_1_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_1_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_1_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_1_sh_availabilityimpact_NONE+=1

            
            
            
    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) < 1.0) and ((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) >=0.0)):
        cvssV3_BASE_score_0_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_0_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_0_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_0_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_0_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_0_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_0_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_0_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_0_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_0_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_0_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_0_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_0_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_0_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_0_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_0_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_0_sh_availabilityimpact_NONE+=1

    elif(((float(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"][j])) == 10.0)):
        cvssV3_BASE_score_10_sh+=1
        
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.1'):
            cvssV3_BASE_score_10_sh_version_3_1+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.version"][j] =='3.0'):
            cvssV3_BASE_score_10_sh_version_3_0+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='NETWORK'):
            cvssV3_BASE_score_10_sh_attackvector_NETWORK+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='LOCAL'):
            cvssV3_BASE_score_10_sh_attackvector_LOCAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='PHYSICAL'):
            cvssV3_BASE_score_10_sh_attackvector_PHYSICAL+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackVector"][j]=='ADJACENT_NETWORK'):
            cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK+=1
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='HIGH'):
            cvssV3_BASE_score_10_sh_attackcomplexity_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='LOW'):
            cvssV3_BASE_score_10_sh_attackcomplexity_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.attackComplexity"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_sh_attackcomplexity_NONE+=1  
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='HIGH'):
            cvssV3_BASE_score_10_sh_privilegesrequired_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='LOW'):
            cvssV3_BASE_score_10_sh_privilegesrequired_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.privilegesRequired"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_sh_privilegesrequired_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.userInteraction"][j]=='REQUIRED'):
            cvssV3_BASE_score_10_sh_userinteraction_REQUIRED+=1
        else:
            cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED+=1
            
        
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='CHANGED'):
            cvssV3_BASE_score_10_sh_scope_CHANGED+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.scope"][j] =='UNCHANGED'):
            cvssV3_BASE_score_10_sh_scope_UNCHANGED+=1
        else:
            cvssV3_BASE_score_10_sh_scope_NONE+=1
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_sh_confidentialityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.confidentialityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_sh_confidentialityimpact_NONE+=1 
            
            
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_sh_integrityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_sh_integrityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.integrityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_sh_integrityimpact_NONE+=1    
            
          
        if(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='HIGH'):
            cvssV3_BASE_score_10_sh_availabilityimpact_HIGH+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='LOW'):
            cvssV3_BASE_score_10_sh_availabilityimpact_LOW+=1
        elif(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"][j]=='MEDIUM'):
            cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM+=1
        else:
            cvssV3_BASE_score_10_sh_availabilityimpact_NONE+=1

            
            
            
print("________________________ESTADÍSTICAS ELEMENTOS VECTOR CVSS3 SEGÚN PUNTUACION BASE CVSSV3 PARTE SMART HOME________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+" VULNERABILIDADES , LAS ESTADISTICAS DE LA RELACION DE ELEMENTOS DEL VECTOR CVSS3 SEGUN PUNTUACION BASE SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_10_sh)+" VULNERABILIDADES LA PUNTUACION BASE ES 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_9_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_8_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_7_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_6_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 Y 7. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_5_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 Y 6. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_4_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 Y 5. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_3_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 Y 4. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_2_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 Y 3. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_1_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 Y 2. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_0_sh)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 Y 1. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")

print("      -    EN  "+str(cvssV3_no_BASE_score_sh)+" VULNERABILIDADES LA PUNTUACIÓN BASE NO ESTÁ DEFINIDA. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")            
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
          
            
            
        
            
print("________________________PORCENTAJES ELEMENTOS VECTOR CVSS3-PUNTUACION BASE CVSSV3 PARTE SMART HOME________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+" VULNERABILIDADES ,  LOS PORCENTAJES DE LA RELACION DE ELEMENTOS DEL VECTOR CVSS3 SEGUN PUNTUACION BASE SON LOS SIGUIENTES:   \n")
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_10_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ES 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_version_3_1*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_version_3_0*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_scope_CHANGED*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_scope_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_10_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_10_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")            
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_9_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_version_3_1*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_version_3_0*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_scope_CHANGED*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_scope_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_9_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_9_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_8_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_version_3_1*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_version_3_0*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_scope_CHANGED*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_scope_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_8_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_8_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_7_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_version_3_1*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_version_3_0*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_scope_CHANGED*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_scope_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_7_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_7_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_6_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 Y 7. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_version_3_1*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_version_3_0*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_scope_CHANGED*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_scope_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_6_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_6_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_5_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 Y 6. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_version_3_1*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_version_3_0*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_scope_CHANGED*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_scope_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_5_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_5_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_4_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 Y 5. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_version_3_1*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_version_3_0*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_scope_CHANGED*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_scope_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_4_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_4_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_BASE_score_3_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 Y 4. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_version_3_1*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_version_3_0*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_scope_CHANGED*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_scope_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_BASE_score_3_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_3_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
print("\n")
if(cvssV3_BASE_score_2_sh>0):
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_2_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 Y 3. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_version_3_1*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_version_3_0*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_scope_CHANGED*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_scope_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_2_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_2_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")  
if(cvssV3_BASE_score_1_sh>0):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_1_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 Y 2. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_version_3_1*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_version_3_0*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_scope_CHANGED*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_scope_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_1_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_1_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")   
if(cvssV3_BASE_score_0_sh):
    print("\n")
    print("      -    EN EL "+str(float(((cvssV3_BASE_score_0_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 Y 1. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_version_3_1*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_version_3_0*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackvector_NETWORK*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackvector_LOCAL*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackvector_PHYSICAL*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackcomplexity_HIGH*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackcomplexity_LOW*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_attackcomplexity_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_privilegesrequired_HIGH*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_privilegesrequired_LOW*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_privilegesrequired_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_userinteraction_REQUIRED*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_scope_CHANGED*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_scope_UNCHANGED*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_scope_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_confidentialityimpact_LOW*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_confidentialityimpact_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_integrityimpact_HIGH*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_integrityimpact_LOW*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_integrityimpact_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_availabilityimpact_HIGH*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_availabilityimpact_LOW*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float(((cvssV3_BASE_score_0_sh_availabilityimpact_NONE*100)/cvssV3_BASE_score_0_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")       
print("\n")
print("      -    EN EL "+str(float(((cvssV3_no_BASE_score_sh*100)/len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"]))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE NO VIENE ESPECIFICADA. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_version_3_1*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_version_3_0*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackvector_NETWORK*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackvector_LOCAL*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackvector_PHYSICAL*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackcomplexity_HIGH*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackcomplexity_LOW*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_attackcomplexity_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_privilegesrequired_HIGH*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_privilegesrequired_LOW*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_privilegesrequired_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_userinteraction_REQUIRED*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_scope_CHANGED*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_scope_UNCHANGED*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_scope_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_confidentialityimpact_LOW*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_confidentialityimpact_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_integrityimpact_HIGH*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_integrityimpact_LOW*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_integrityimpact_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_availabilityimpact_HIGH*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_availabilityimpact_LOW*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float(((cvssV3_no_BASE_score_sh_availabilityimpact_NONE*100)/cvssV3_no_BASE_score_sh)))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")       
            
            
        
            
       

    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
print("________________________ESTADÍSTICAS ELEMENTOS VECTOR CVSS3-PUNTUACION BASE CVSSV3PARTE IOT Y SMART HOME CONJUNTAS ________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))+" VULNERABILIDADES , LAS ESTADISTICAS DE ELEMENTOS DEL VECTOR CVSS3 SEGUND PUNTUACION DE BASE SON LAS SIGUIENTES:  \n")
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot)+" VULNERABILIDADES LA PUNTUACION BASE ES 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_version_3_1+cvssV3_BASE_score_10_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_version_3_0+cvssV3_BASE_score_10_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_NETWORK+cvssV3_BASE_score_10_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_LOCAL+cvssV3_BASE_score_10_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_PHYSICAL+cvssV3_BASE_score_10_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_HIGH+cvssV3_BASE_score_10_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_LOW+cvssV3_BASE_score_10_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_attackcomplexity_NONE+cvssV3_BASE_score_10_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_HIGH+cvssV3_BASE_score_10_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_LOW+cvssV3_BASE_score_10_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_privilegesrequired_NONE+cvssV3_BASE_score_10_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_userinteraction_REQUIRED+cvssV3_BASE_score_10_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_CHANGED+cvssV3_BASE_score_10_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_UNCHANGED+cvssV3_BASE_score_10_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_scope_NONE+cvssV3_BASE_score_10_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_LOW+cvssV3_BASE_score_10_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_confidentialityimpact_NONE+cvssV3_BASE_score_10_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_HIGH+cvssV3_BASE_score_10_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_LOW+cvssV3_BASE_score_10_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_integrityimpact_NONE+cvssV3_BASE_score_10_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_HIGH+cvssV3_BASE_score_10_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_LOW+cvssV3_BASE_score_10_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_10_sh_availabilityimpact_NONE+cvssV3_BASE_score_10_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            

print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_version_3_1+cvssV3_BASE_score_9_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_version_3_0+cvssV3_BASE_score_9_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_NETWORK+cvssV3_BASE_score_9_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_LOCAL+cvssV3_BASE_score_9_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_PHYSICAL+cvssV3_BASE_score_9_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_HIGH+cvssV3_BASE_score_9_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_LOW+cvssV3_BASE_score_9_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_attackcomplexity_NONE+cvssV3_BASE_score_9_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_HIGH+cvssV3_BASE_score_9_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_LOW+cvssV3_BASE_score_9_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_privilegesrequired_NONE+cvssV3_BASE_score_9_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_userinteraction_REQUIRED+cvssV3_BASE_score_9_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_CHANGED+cvssV3_BASE_score_9_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_UNCHANGED+cvssV3_BASE_score_9_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_scope_NONE+cvssV3_BASE_score_9_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_LOW+cvssV3_BASE_score_9_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_confidentialityimpact_NONE+cvssV3_BASE_score_9_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_HIGH+cvssV3_BASE_score_9_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_LOW+cvssV3_BASE_score_9_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_integrityimpact_NONE+cvssV3_BASE_score_9_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_HIGH+cvssV3_BASE_score_9_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_LOW+cvssV3_BASE_score_9_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_9_sh_availabilityimpact_NONE+cvssV3_BASE_score_9_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_version_3_1+cvssV3_BASE_score_8_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_version_3_0+cvssV3_BASE_score_8_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_NETWORK+cvssV3_BASE_score_8_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_LOCAL+cvssV3_BASE_score_8_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_PHYSICAL+cvssV3_BASE_score_8_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_HIGH+cvssV3_BASE_score_8_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_LOW+cvssV3_BASE_score_8_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_attackcomplexity_NONE+cvssV3_BASE_score_8_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_HIGH+cvssV3_BASE_score_8_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_LOW+cvssV3_BASE_score_8_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_privilegesrequired_NONE+cvssV3_BASE_score_8_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_userinteraction_REQUIRED+cvssV3_BASE_score_8_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_CHANGED+cvssV3_BASE_score_8_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_UNCHANGED+cvssV3_BASE_score_8_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_scope_NONE+cvssV3_BASE_score_8_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_LOW+cvssV3_BASE_score_8_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_confidentialityimpact_NONE+cvssV3_BASE_score_8_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_HIGH+cvssV3_BASE_score_8_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_LOW+cvssV3_BASE_score_8_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_integrityimpact_NONE+cvssV3_BASE_score_8_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_HIGH+cvssV3_BASE_score_8_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_LOW+cvssV3_BASE_score_8_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_8_sh_availabilityimpact_NONE+cvssV3_BASE_score_8_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       


print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 Y 8. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_version_3_1+cvssV3_BASE_score_7_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_version_3_0+cvssV3_BASE_score_7_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_NETWORK+cvssV3_BASE_score_7_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_LOCAL+cvssV3_BASE_score_7_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_PHYSICAL+cvssV3_BASE_score_7_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_HIGH+cvssV3_BASE_score_7_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_LOW+cvssV3_BASE_score_7_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_attackcomplexity_NONE+cvssV3_BASE_score_7_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_HIGH+cvssV3_BASE_score_7_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_LOW+cvssV3_BASE_score_7_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_privilegesrequired_NONE+cvssV3_BASE_score_7_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_userinteraction_REQUIRED+cvssV3_BASE_score_7_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_CHANGED+cvssV3_BASE_score_7_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_UNCHANGED+cvssV3_BASE_score_7_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_scope_NONE+cvssV3_BASE_score_7_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_LOW+cvssV3_BASE_score_7_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_confidentialityimpact_NONE+cvssV3_BASE_score_7_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_HIGH+cvssV3_BASE_score_7_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_LOW+cvssV3_BASE_score_7_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_integrityimpact_NONE+cvssV3_BASE_score_7_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_HIGH+cvssV3_BASE_score_7_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_LOW+cvssV3_BASE_score_7_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_7_sh_availabilityimpact_NONE+cvssV3_BASE_score_7_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_version_3_1+cvssV3_BASE_score_6_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_version_3_0+cvssV3_BASE_score_6_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_NETWORK+cvssV3_BASE_score_6_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_LOCAL+cvssV3_BASE_score_6_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_PHYSICAL+cvssV3_BASE_score_6_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_HIGH+cvssV3_BASE_score_6_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_LOW+cvssV3_BASE_score_6_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_attackcomplexity_NONE+cvssV3_BASE_score_6_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_HIGH+cvssV3_BASE_score_6_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_LOW+cvssV3_BASE_score_6_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_privilegesrequired_NONE+cvssV3_BASE_score_6_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_userinteraction_REQUIRED+cvssV3_BASE_score_6_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_CHANGED+cvssV3_BASE_score_6_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_UNCHANGED+cvssV3_BASE_score_6_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_scope_NONE+cvssV3_BASE_score_6_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_LOW+cvssV3_BASE_score_6_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_confidentialityimpact_NONE+cvssV3_BASE_score_6_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_HIGH+cvssV3_BASE_score_6_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_LOW+cvssV3_BASE_score_6_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_integrityimpact_NONE+cvssV3_BASE_score_6_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_HIGH+cvssV3_BASE_score_6_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_LOW+cvssV3_BASE_score_6_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_6_sh_availabilityimpact_NONE+cvssV3_BASE_score_6_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_version_3_1+cvssV3_BASE_score_5_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_version_3_0+cvssV3_BASE_score_5_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_NETWORK+cvssV3_BASE_score_5_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_LOCAL+cvssV3_BASE_score_5_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_PHYSICAL+cvssV3_BASE_score_5_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_HIGH+cvssV3_BASE_score_5_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_LOW+cvssV3_BASE_score_5_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_attackcomplexity_NONE+cvssV3_BASE_score_5_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_HIGH+cvssV3_BASE_score_5_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_LOW+cvssV3_BASE_score_5_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_privilegesrequired_NONE+cvssV3_BASE_score_5_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_userinteraction_REQUIRED+cvssV3_BASE_score_5_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_CHANGED+cvssV3_BASE_score_5_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_UNCHANGED+cvssV3_BASE_score_5_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_scope_NONE+cvssV3_BASE_score_5_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_LOW+cvssV3_BASE_score_5_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_confidentialityimpact_NONE+cvssV3_BASE_score_5_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_HIGH+cvssV3_BASE_score_5_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_LOW+cvssV3_BASE_score_5_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_integrityimpact_NONE+cvssV3_BASE_score_5_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_HIGH+cvssV3_BASE_score_5_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_LOW+cvssV3_BASE_score_5_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_5_sh_availabilityimpact_NONE+cvssV3_BASE_score_5_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_version_3_1+cvssV3_BASE_score_4_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_version_3_0+cvssV3_BASE_score_4_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_NETWORK+cvssV3_BASE_score_4_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_LOCAL+cvssV3_BASE_score_4_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_PHYSICAL+cvssV3_BASE_score_4_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_HIGH+cvssV3_BASE_score_4_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_LOW+cvssV3_BASE_score_4_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_attackcomplexity_NONE+cvssV3_BASE_score_4_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_HIGH+cvssV3_BASE_score_4_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_LOW+cvssV3_BASE_score_4_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_privilegesrequired_NONE+cvssV3_BASE_score_4_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_userinteraction_REQUIRED+cvssV3_BASE_score_4_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_CHANGED+cvssV3_BASE_score_4_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_UNCHANGED+cvssV3_BASE_score_4_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_scope_NONE+cvssV3_BASE_score_4_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_LOW+cvssV3_BASE_score_4_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_confidentialityimpact_NONE+cvssV3_BASE_score_4_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_HIGH+cvssV3_BASE_score_4_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_LOW+cvssV3_BASE_score_4_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_integrityimpact_NONE+cvssV3_BASE_score_4_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_HIGH+cvssV3_BASE_score_4_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_LOW+cvssV3_BASE_score_4_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_4_sh_availabilityimpact_NONE+cvssV3_BASE_score_4_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_version_3_1+cvssV3_BASE_score_3_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_version_3_0+cvssV3_BASE_score_3_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_NETWORK+cvssV3_BASE_score_3_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_LOCAL+cvssV3_BASE_score_3_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_PHYSICAL+cvssV3_BASE_score_3_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_HIGH+cvssV3_BASE_score_3_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_LOW+cvssV3_BASE_score_3_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_attackcomplexity_NONE+cvssV3_BASE_score_3_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_HIGH+cvssV3_BASE_score_3_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_LOW+cvssV3_BASE_score_3_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_privilegesrequired_NONE+cvssV3_BASE_score_3_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_userinteraction_REQUIRED+cvssV3_BASE_score_3_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_CHANGED+cvssV3_BASE_score_3_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_UNCHANGED+cvssV3_BASE_score_3_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_scope_NONE+cvssV3_BASE_score_3_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_LOW+cvssV3_BASE_score_3_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_confidentialityimpact_NONE+cvssV3_BASE_score_3_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_HIGH+cvssV3_BASE_score_3_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_LOW+cvssV3_BASE_score_3_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_integrityimpact_NONE+cvssV3_BASE_score_3_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_HIGH+cvssV3_BASE_score_3_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_LOW+cvssV3_BASE_score_3_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_3_sh_availabilityimpact_NONE+cvssV3_BASE_score_3_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            

print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_version_3_1+cvssV3_BASE_score_2_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_version_3_0+cvssV3_BASE_score_2_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_NETWORK+cvssV3_BASE_score_2_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_LOCAL+cvssV3_BASE_score_2_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_PHYSICAL+cvssV3_BASE_score_2_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_HIGH+cvssV3_BASE_score_2_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_LOW+cvssV3_BASE_score_2_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_attackcomplexity_NONE+cvssV3_BASE_score_2_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_HIGH+cvssV3_BASE_score_2_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_LOW+cvssV3_BASE_score_2_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_privilegesrequired_NONE+cvssV3_BASE_score_2_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_userinteraction_REQUIRED+cvssV3_BASE_score_2_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_CHANGED+cvssV3_BASE_score_2_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_UNCHANGED+cvssV3_BASE_score_2_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_scope_NONE+cvssV3_BASE_score_2_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_LOW+cvssV3_BASE_score_2_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_confidentialityimpact_NONE+cvssV3_BASE_score_2_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_HIGH+cvssV3_BASE_score_2_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_LOW+cvssV3_BASE_score_2_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_integrityimpact_NONE+cvssV3_BASE_score_2_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_HIGH+cvssV3_BASE_score_2_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_LOW+cvssV3_BASE_score_2_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_2_sh_availabilityimpact_NONE+cvssV3_BASE_score_2_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_version_3_1+cvssV3_BASE_score_1_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_version_3_0+cvssV3_BASE_score_1_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_NETWORK+cvssV3_BASE_score_1_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_LOCAL+cvssV3_BASE_score_1_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_PHYSICAL+cvssV3_BASE_score_1_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_HIGH+cvssV3_BASE_score_1_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_LOW+cvssV3_BASE_score_1_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_attackcomplexity_NONE+cvssV3_BASE_score_1_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_HIGH+cvssV3_BASE_score_1_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_LOW+cvssV3_BASE_score_1_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_privilegesrequired_NONE+cvssV3_BASE_score_1_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_userinteraction_REQUIRED+cvssV3_BASE_score_1_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_CHANGED+cvssV3_BASE_score_1_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_UNCHANGED+cvssV3_BASE_score_1_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_scope_NONE+cvssV3_BASE_score_1_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_LOW+cvssV3_BASE_score_1_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_confidentialityimpact_NONE+cvssV3_BASE_score_1_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_HIGH+cvssV3_BASE_score_1_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_LOW+cvssV3_BASE_score_1_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_integrityimpact_NONE+cvssV3_BASE_score_1_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_HIGH+cvssV3_BASE_score_1_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_LOW+cvssV3_BASE_score_1_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_1_sh_availabilityimpact_NONE+cvssV3_BASE_score_1_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot)+" VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_version_3_1+cvssV3_BASE_score_0_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_version_3_0+cvssV3_BASE_score_0_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_NETWORK+cvssV3_BASE_score_0_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_LOCAL+cvssV3_BASE_score_0_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_PHYSICAL+cvssV3_BASE_score_0_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_HIGH+cvssV3_BASE_score_0_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_LOW+cvssV3_BASE_score_0_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_attackcomplexity_NONE+cvssV3_BASE_score_0_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_HIGH+cvssV3_BASE_score_0_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_LOW+cvssV3_BASE_score_0_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_privilegesrequired_NONE+cvssV3_BASE_score_0_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_userinteraction_REQUIRED+cvssV3_BASE_score_0_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_CHANGED+cvssV3_BASE_score_0_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_UNCHANGED+cvssV3_BASE_score_0_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_scope_NONE+cvssV3_BASE_score_0_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_LOW+cvssV3_BASE_score_0_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_confidentialityimpact_NONE+cvssV3_BASE_score_0_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_HIGH+cvssV3_BASE_score_0_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_LOW+cvssV3_BASE_score_0_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_integrityimpact_NONE+cvssV3_BASE_score_0_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_HIGH+cvssV3_BASE_score_0_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_LOW+cvssV3_BASE_score_0_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_BASE_score_0_sh_availabilityimpact_NONE+cvssV3_BASE_score_0_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       
            
    
print("\n")
print("      -    EN  "+str(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot)+" VULNERABILIDADES LA PUNTUACION BASE NO ESTÁ ESPECIFICADA. LAS ESTADÍSTICAS DEL VECTOR CVSS3 SON LAS SIGUIENTES:  \n")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_version_3_1+cvssV3_no_BASE_score_iot_version_3_1)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_version_3_0+cvssV3_no_BASE_score_iot_version_3_0)+" VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_NETWORK+cvssV3_no_BASE_score_iot_attackvector_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_LOCAL+cvssV3_no_BASE_score_iot_attackvector_LOCAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_PHYSICAL+cvssV3_no_BASE_score_iot_attackvector_PHYSICAL)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK+cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK)+" VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_HIGH+cvssV3_no_BASE_score_iot_attackcomplexity_HIGH)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_LOW+cvssV3_no_BASE_score_iot_attackcomplexity_LOW)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM+cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_attackcomplexity_NONE+cvssV3_no_BASE_score_iot_attackcomplexity_NONE)+" VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_HIGH+cvssV3_no_BASE_score_iot_privilegesrequired_HIGH)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_LOW+cvssV3_no_BASE_score_iot_privilegesrequired_LOW)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM+cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM)+" VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_privilegesrequired_NONE+cvssV3_no_BASE_score_iot_privilegesrequired_NONE)+" VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_userinteraction_REQUIRED+cvssV3_no_BASE_score_iot_userinteraction_REQUIRED)+" VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED+cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED)+" VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_CHANGED+cvssV3_no_BASE_score_iot_scope_CHANGED)+" VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_UNCHANGED+cvssV3_no_BASE_score_iot_scope_UNCHANGED)+" VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_scope_NONE+cvssV3_no_BASE_score_iot_scope_NONE)+" VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH+cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_LOW+cvssV3_no_BASE_score_iot_confidentialityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM+cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_confidentialityimpact_NONE+cvssV3_no_BASE_score_iot_confidentialityimpact_NONE)+" VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_HIGH+cvssV3_no_BASE_score_iot_integrityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_LOW+cvssV3_no_BASE_score_iot_integrityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM+cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_integrityimpact_NONE+cvssV3_no_BASE_score_iot_integrityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_HIGH+cvssV3_no_BASE_score_iot_availabilityimpact_HIGH)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_LOW+cvssV3_no_BASE_score_iot_availabilityimpact_LOW)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM+cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM)+" VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN  "+str(cvssV3_no_BASE_score_sh_availabilityimpact_NONE+cvssV3_no_BASE_score_iot_availabilityimpact_NONE)+" VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")       










print("________________________PORCENTAJES ELEMENTOS VECTOR CVSS3-PUNTUACION BASE CVSSV3 PARTE IOT Y SMART HOME CONJUNTAS________________________")
print("\n")        
            
            
    
print("\n")
print(" DE UN TOTAL DE "+str((len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"]))+(len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.availabilityImpact"])))+" VULNERABILIDADES , LOS PORCENTAJES DE ELEMENTOS DEL VECTOR CVSS3 SEGUN PUNTUACION DE BASE SON LOS SIGUIENTES:  \n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ES 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_version_3_1+cvssV3_BASE_score_10_iot_version_3_1)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_version_3_0+cvssV3_BASE_score_10_iot_version_3_0)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackvector_NETWORK+cvssV3_BASE_score_10_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackvector_LOCAL+cvssV3_BASE_score_10_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackvector_PHYSICAL+cvssV3_BASE_score_10_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_10_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackcomplexity_HIGH+cvssV3_BASE_score_10_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackcomplexity_LOW+cvssV3_BASE_score_10_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_10_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_attackcomplexity_NONE+cvssV3_BASE_score_10_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_privilegesrequired_HIGH+cvssV3_BASE_score_10_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_privilegesrequired_LOW+cvssV3_BASE_score_10_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_10_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_privilegesrequired_NONE+cvssV3_BASE_score_10_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_userinteraction_REQUIRED+cvssV3_BASE_score_10_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_10_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_scope_CHANGED+cvssV3_BASE_score_10_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_scope_UNCHANGED+cvssV3_BASE_score_10_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_scope_NONE+cvssV3_BASE_score_10_iot_scope_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_10_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_confidentialityimpact_LOW+cvssV3_BASE_score_10_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_10_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_confidentialityimpact_NONE+cvssV3_BASE_score_10_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_integrityimpact_HIGH+cvssV3_BASE_score_10_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_integrityimpact_LOW+cvssV3_BASE_score_10_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_10_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_integrityimpact_NONE+cvssV3_BASE_score_10_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_availabilityimpact_HIGH+cvssV3_BASE_score_10_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_availabilityimpact_LOW+cvssV3_BASE_score_10_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_10_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_10_sh_availabilityimpact_NONE+cvssV3_BASE_score_10_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_10_sh+cvssV3_BASE_score_10_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 9 Y 10. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_version_3_1+cvssV3_BASE_score_9_iot_version_3_1)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_version_3_0+cvssV3_BASE_score_9_iot_version_3_0)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackvector_NETWORK+cvssV3_BASE_score_9_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackvector_LOCAL+cvssV3_BASE_score_9_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackvector_PHYSICAL+cvssV3_BASE_score_9_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_9_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackcomplexity_HIGH+cvssV3_BASE_score_9_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackcomplexity_LOW+cvssV3_BASE_score_9_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_9_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_attackcomplexity_NONE+cvssV3_BASE_score_9_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_privilegesrequired_HIGH+cvssV3_BASE_score_9_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_privilegesrequired_LOW+cvssV3_BASE_score_9_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_9_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_privilegesrequired_NONE+cvssV3_BASE_score_9_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_userinteraction_REQUIRED+cvssV3_BASE_score_9_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_9_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_scope_CHANGED+cvssV3_BASE_score_9_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_scope_UNCHANGED+cvssV3_BASE_score_9_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_scope_NONE+cvssV3_BASE_score_9_iot_scope_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_9_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_confidentialityimpact_LOW+cvssV3_BASE_score_9_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_9_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_confidentialityimpact_NONE+cvssV3_BASE_score_9_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_integrityimpact_HIGH+cvssV3_BASE_score_9_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_integrityimpact_LOW+cvssV3_BASE_score_9_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_9_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_integrityimpact_NONE+cvssV3_BASE_score_9_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_availabilityimpact_HIGH+cvssV3_BASE_score_9_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_availabilityimpact_LOW+cvssV3_BASE_score_9_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_9_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_9_sh_availabilityimpact_NONE+cvssV3_BASE_score_9_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_9_sh+cvssV3_BASE_score_9_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 8 Y 9. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_version_3_1+cvssV3_BASE_score_8_iot_version_3_1)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_version_3_0+cvssV3_BASE_score_8_iot_version_3_0)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackvector_NETWORK+cvssV3_BASE_score_8_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackvector_LOCAL+cvssV3_BASE_score_8_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackvector_PHYSICAL+cvssV3_BASE_score_8_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_8_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackcomplexity_HIGH+cvssV3_BASE_score_8_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackcomplexity_LOW+cvssV3_BASE_score_8_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_8_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_attackcomplexity_NONE+cvssV3_BASE_score_8_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_privilegesrequired_HIGH+cvssV3_BASE_score_8_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_privilegesrequired_LOW+cvssV3_BASE_score_8_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_8_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_privilegesrequired_NONE+cvssV3_BASE_score_8_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_userinteraction_REQUIRED+cvssV3_BASE_score_8_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_8_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_scope_CHANGED+cvssV3_BASE_score_8_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_scope_UNCHANGED+cvssV3_BASE_score_8_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_scope_NONE+cvssV3_BASE_score_8_iot_scope_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_8_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_confidentialityimpact_LOW+cvssV3_BASE_score_8_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_8_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_confidentialityimpact_NONE+cvssV3_BASE_score_8_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_integrityimpact_HIGH+cvssV3_BASE_score_8_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_integrityimpact_LOW+cvssV3_BASE_score_8_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_8_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_integrityimpact_NONE+cvssV3_BASE_score_8_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_availabilityimpact_HIGH+cvssV3_BASE_score_8_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_availabilityimpact_LOW+cvssV3_BASE_score_8_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_8_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_8_sh_availabilityimpact_NONE+cvssV3_BASE_score_8_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_8_sh+cvssV3_BASE_score_8_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 7 y 8. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_version_3_1+cvssV3_BASE_score_7_iot_version_3_1)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_version_3_0+cvssV3_BASE_score_7_iot_version_3_0)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackvector_NETWORK+cvssV3_BASE_score_7_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackvector_LOCAL+cvssV3_BASE_score_7_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackvector_PHYSICAL+cvssV3_BASE_score_7_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_7_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackcomplexity_HIGH+cvssV3_BASE_score_7_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackcomplexity_LOW+cvssV3_BASE_score_7_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_7_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_attackcomplexity_NONE+cvssV3_BASE_score_7_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_privilegesrequired_HIGH+cvssV3_BASE_score_7_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_privilegesrequired_LOW+cvssV3_BASE_score_7_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_7_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_privilegesrequired_NONE+cvssV3_BASE_score_7_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_userinteraction_REQUIRED+cvssV3_BASE_score_7_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_7_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_scope_CHANGED+cvssV3_BASE_score_7_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_scope_UNCHANGED+cvssV3_BASE_score_7_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_scope_NONE+cvssV3_BASE_score_7_iot_scope_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_7_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_confidentialityimpact_LOW+cvssV3_BASE_score_7_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_7_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_confidentialityimpact_NONE+cvssV3_BASE_score_7_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_integrityimpact_HIGH+cvssV3_BASE_score_7_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_integrityimpact_LOW+cvssV3_BASE_score_7_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_7_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_integrityimpact_NONE+cvssV3_BASE_score_7_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_availabilityimpact_HIGH+cvssV3_BASE_score_7_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_availabilityimpact_LOW+cvssV3_BASE_score_7_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_7_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_7_sh_availabilityimpact_NONE+cvssV3_BASE_score_7_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_7_sh+cvssV3_BASE_score_7_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 6 y 7. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_version_3_1+cvssV3_BASE_score_6_iot_version_3_1)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_version_3_0+cvssV3_BASE_score_6_iot_version_3_0)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackvector_NETWORK+cvssV3_BASE_score_6_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackvector_LOCAL+cvssV3_BASE_score_6_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackvector_PHYSICAL+cvssV3_BASE_score_6_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_6_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackcomplexity_HIGH+cvssV3_BASE_score_6_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackcomplexity_LOW+cvssV3_BASE_score_6_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_6_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_attackcomplexity_NONE+cvssV3_BASE_score_6_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_privilegesrequired_HIGH+cvssV3_BASE_score_6_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_privilegesrequired_LOW+cvssV3_BASE_score_6_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_6_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_privilegesrequired_NONE+cvssV3_BASE_score_6_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_userinteraction_REQUIRED+cvssV3_BASE_score_6_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_6_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_scope_CHANGED+cvssV3_BASE_score_6_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_scope_UNCHANGED+cvssV3_BASE_score_6_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_scope_NONE+cvssV3_BASE_score_6_iot_scope_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_6_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_confidentialityimpact_LOW+cvssV3_BASE_score_6_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_6_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_confidentialityimpact_NONE+cvssV3_BASE_score_6_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_integrityimpact_HIGH+cvssV3_BASE_score_6_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_integrityimpact_LOW+cvssV3_BASE_score_6_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_6_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_integrityimpact_NONE+cvssV3_BASE_score_6_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_availabilityimpact_HIGH+cvssV3_BASE_score_6_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_availabilityimpact_LOW+cvssV3_BASE_score_6_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_6_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_6_sh_availabilityimpact_NONE+cvssV3_BASE_score_6_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_6_sh+cvssV3_BASE_score_6_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 5 y 6. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_version_3_1+cvssV3_BASE_score_5_iot_version_3_1)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_version_3_0+cvssV3_BASE_score_5_iot_version_3_0)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackvector_NETWORK+cvssV3_BASE_score_5_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackvector_LOCAL+cvssV3_BASE_score_5_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackvector_PHYSICAL+cvssV3_BASE_score_5_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_5_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackcomplexity_HIGH+cvssV3_BASE_score_5_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackcomplexity_LOW+cvssV3_BASE_score_5_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_5_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_attackcomplexity_NONE+cvssV3_BASE_score_5_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_privilegesrequired_HIGH+cvssV3_BASE_score_5_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_privilegesrequired_LOW+cvssV3_BASE_score_5_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_5_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_privilegesrequired_NONE+cvssV3_BASE_score_5_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_userinteraction_REQUIRED+cvssV3_BASE_score_5_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_5_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_scope_CHANGED+cvssV3_BASE_score_5_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_scope_UNCHANGED+cvssV3_BASE_score_5_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_scope_NONE+cvssV3_BASE_score_5_iot_scope_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_5_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_confidentialityimpact_LOW+cvssV3_BASE_score_5_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_5_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_confidentialityimpact_NONE+cvssV3_BASE_score_5_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_integrityimpact_HIGH+cvssV3_BASE_score_5_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_integrityimpact_LOW+cvssV3_BASE_score_5_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_5_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_integrityimpact_NONE+cvssV3_BASE_score_5_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_availabilityimpact_HIGH+cvssV3_BASE_score_5_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_availabilityimpact_LOW+cvssV3_BASE_score_5_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_5_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_5_sh_availabilityimpact_NONE+cvssV3_BASE_score_5_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_5_sh+cvssV3_BASE_score_5_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 4 y 5. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_version_3_1+cvssV3_BASE_score_4_iot_version_3_1)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_version_3_0+cvssV3_BASE_score_4_iot_version_3_0)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackvector_NETWORK+cvssV3_BASE_score_4_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackvector_LOCAL+cvssV3_BASE_score_4_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackvector_PHYSICAL+cvssV3_BASE_score_4_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_4_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackcomplexity_HIGH+cvssV3_BASE_score_4_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackcomplexity_LOW+cvssV3_BASE_score_4_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_4_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_attackcomplexity_NONE+cvssV3_BASE_score_4_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_privilegesrequired_HIGH+cvssV3_BASE_score_4_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_privilegesrequired_LOW+cvssV3_BASE_score_4_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_4_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_privilegesrequired_NONE+cvssV3_BASE_score_4_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_userinteraction_REQUIRED+cvssV3_BASE_score_4_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_4_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_scope_CHANGED+cvssV3_BASE_score_4_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_scope_UNCHANGED+cvssV3_BASE_score_4_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_scope_NONE+cvssV3_BASE_score_4_iot_scope_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_4_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_confidentialityimpact_LOW+cvssV3_BASE_score_4_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_4_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_confidentialityimpact_NONE+cvssV3_BASE_score_4_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_integrityimpact_HIGH+cvssV3_BASE_score_4_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_integrityimpact_LOW+cvssV3_BASE_score_4_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_4_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_integrityimpact_NONE+cvssV3_BASE_score_4_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_availabilityimpact_HIGH+cvssV3_BASE_score_4_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_availabilityimpact_LOW+cvssV3_BASE_score_4_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_4_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_4_sh_availabilityimpact_NONE+cvssV3_BASE_score_4_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_4_sh+cvssV3_BASE_score_4_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
print("      -    EN EL "+str(float((((cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 3 y 4. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_version_3_1+cvssV3_BASE_score_3_iot_version_3_1)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_version_3_0+cvssV3_BASE_score_3_iot_version_3_0)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackvector_NETWORK+cvssV3_BASE_score_3_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackvector_LOCAL+cvssV3_BASE_score_3_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackvector_PHYSICAL+cvssV3_BASE_score_3_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_3_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackcomplexity_HIGH+cvssV3_BASE_score_3_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackcomplexity_LOW+cvssV3_BASE_score_3_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_3_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_attackcomplexity_NONE+cvssV3_BASE_score_3_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_privilegesrequired_HIGH+cvssV3_BASE_score_3_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_privilegesrequired_LOW+cvssV3_BASE_score_3_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_3_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_privilegesrequired_NONE+cvssV3_BASE_score_3_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_userinteraction_REQUIRED+cvssV3_BASE_score_3_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_3_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_scope_CHANGED+cvssV3_BASE_score_3_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_scope_UNCHANGED+cvssV3_BASE_score_3_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_scope_NONE+cvssV3_BASE_score_3_iot_scope_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_3_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_confidentialityimpact_LOW+cvssV3_BASE_score_3_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_3_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_confidentialityimpact_NONE+cvssV3_BASE_score_3_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_integrityimpact_HIGH+cvssV3_BASE_score_3_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_integrityimpact_LOW+cvssV3_BASE_score_3_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_3_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_integrityimpact_NONE+cvssV3_BASE_score_3_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_availabilityimpact_HIGH+cvssV3_BASE_score_3_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_availabilityimpact_LOW+cvssV3_BASE_score_3_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_3_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_BASE_score_3_sh_availabilityimpact_NONE+cvssV3_BASE_score_3_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_3_sh+cvssV3_BASE_score_3_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")
if((cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot)>0):
    print("      -    EN EL "+str(float((((cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 2 y 3. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_version_3_1+cvssV3_BASE_score_2_iot_version_3_1)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_version_3_0+cvssV3_BASE_score_2_iot_version_3_0)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackvector_NETWORK+cvssV3_BASE_score_2_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackvector_LOCAL+cvssV3_BASE_score_2_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackvector_PHYSICAL+cvssV3_BASE_score_2_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_2_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackcomplexity_HIGH+cvssV3_BASE_score_2_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackcomplexity_LOW+cvssV3_BASE_score_2_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_2_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_attackcomplexity_NONE+cvssV3_BASE_score_2_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_privilegesrequired_HIGH+cvssV3_BASE_score_2_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_privilegesrequired_LOW+cvssV3_BASE_score_2_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_2_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_privilegesrequired_NONE+cvssV3_BASE_score_2_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_userinteraction_REQUIRED+cvssV3_BASE_score_2_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_2_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_scope_CHANGED+cvssV3_BASE_score_2_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_scope_UNCHANGED+cvssV3_BASE_score_2_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_scope_NONE+cvssV3_BASE_score_2_iot_scope_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_2_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_confidentialityimpact_LOW+cvssV3_BASE_score_2_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_2_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_confidentialityimpact_NONE+cvssV3_BASE_score_2_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_integrityimpact_HIGH+cvssV3_BASE_score_2_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_integrityimpact_LOW+cvssV3_BASE_score_2_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_2_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_integrityimpact_NONE+cvssV3_BASE_score_2_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_availabilityimpact_HIGH+cvssV3_BASE_score_2_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_availabilityimpact_LOW+cvssV3_BASE_score_2_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_2_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_2_sh_availabilityimpact_NONE+cvssV3_BASE_score_2_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_2_sh+cvssV3_BASE_score_2_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
if((cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot)):
    print("      -    EN EL "+str(float((((cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 1 y 2. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_version_3_1+cvssV3_BASE_score_1_iot_version_3_1)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_version_3_0+cvssV3_BASE_score_1_iot_version_3_0)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackvector_NETWORK+cvssV3_BASE_score_1_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackvector_LOCAL+cvssV3_BASE_score_1_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackvector_PHYSICAL+cvssV3_BASE_score_1_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_1_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackcomplexity_HIGH+cvssV3_BASE_score_1_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackcomplexity_LOW+cvssV3_BASE_score_1_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_1_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_attackcomplexity_NONE+cvssV3_BASE_score_1_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_privilegesrequired_HIGH+cvssV3_BASE_score_1_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_privilegesrequired_LOW+cvssV3_BASE_score_1_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_1_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_privilegesrequired_NONE+cvssV3_BASE_score_1_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_userinteraction_REQUIRED+cvssV3_BASE_score_1_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_1_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_scope_CHANGED+cvssV3_BASE_score_1_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_scope_UNCHANGED+cvssV3_BASE_score_1_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_scope_NONE+cvssV3_BASE_score_1_iot_scope_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_1_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_confidentialityimpact_LOW+cvssV3_BASE_score_1_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_1_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_confidentialityimpact_NONE+cvssV3_BASE_score_1_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_integrityimpact_HIGH+cvssV3_BASE_score_1_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_integrityimpact_LOW+cvssV3_BASE_score_1_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_1_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_integrityimpact_NONE+cvssV3_BASE_score_1_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_availabilityimpact_HIGH+cvssV3_BASE_score_1_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_availabilityimpact_LOW+cvssV3_BASE_score_1_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_1_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_1_sh_availabilityimpact_NONE+cvssV3_BASE_score_1_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_1_sh+cvssV3_BASE_score_1_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
if((cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot)):
    print("      -    EN EL "+str(float((((cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE ESTÁ ENTRE 0 y 1. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_version_3_1+cvssV3_BASE_score_0_iot_version_3_1)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_version_3_0+cvssV3_BASE_score_0_iot_version_3_0)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackvector_NETWORK+cvssV3_BASE_score_0_iot_attackvector_NETWORK)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackvector_LOCAL+cvssV3_BASE_score_0_iot_attackvector_LOCAL)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackvector_PHYSICAL+cvssV3_BASE_score_0_iot_attackvector_PHYSICAL)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackvector_ADJACENT_NETWORK+cvssV3_BASE_score_0_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackcomplexity_HIGH+cvssV3_BASE_score_0_iot_attackcomplexity_HIGH)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackcomplexity_LOW+cvssV3_BASE_score_0_iot_attackcomplexity_LOW)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackcomplexity_MEDIUM+cvssV3_BASE_score_0_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_attackcomplexity_NONE+cvssV3_BASE_score_0_iot_attackcomplexity_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_privilegesrequired_HIGH+cvssV3_BASE_score_0_iot_privilegesrequired_HIGH)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_privilegesrequired_LOW+cvssV3_BASE_score_0_iot_privilegesrequired_LOW)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_privilegesrequired_MEDIUM+cvssV3_BASE_score_0_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_privilegesrequired_NONE+cvssV3_BASE_score_0_iot_privilegesrequired_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_userinteraction_REQUIRED+cvssV3_BASE_score_0_iot_userinteraction_REQUIRED)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_userinteraction_NONEREQUIRED+cvssV3_BASE_score_0_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_scope_CHANGED+cvssV3_BASE_score_0_iot_scope_CHANGED)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_scope_UNCHANGED+cvssV3_BASE_score_0_iot_scope_UNCHANGED)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_scope_NONE+cvssV3_BASE_score_0_iot_scope_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_confidentialityimpact_HIGH+cvssV3_BASE_score_0_iot_confidentialityimpact_HIGH)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_confidentialityimpact_LOW+cvssV3_BASE_score_0_iot_confidentialityimpact_LOW)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_confidentialityimpact_MEDIUM+cvssV3_BASE_score_0_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_confidentialityimpact_NONE+cvssV3_BASE_score_0_iot_confidentialityimpact_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_integrityimpact_HIGH+cvssV3_BASE_score_0_iot_integrityimpact_HIGH)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_integrityimpact_LOW+cvssV3_BASE_score_0_iot_integrityimpact_LOW)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_integrityimpact_MEDIUM+cvssV3_BASE_score_0_iot_integrityimpact_MEDIUM)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_integrityimpact_NONE+cvssV3_BASE_score_0_iot_integrityimpact_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
    print("\n")
    print("\n")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_availabilityimpact_HIGH+cvssV3_BASE_score_0_iot_availabilityimpact_HIGH)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_availabilityimpact_LOW+cvssV3_BASE_score_0_iot_availabilityimpact_LOW)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_availabilityimpact_MEDIUM+cvssV3_BASE_score_0_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
    print("            -    EN EL "+str(float((((cvssV3_BASE_score_0_sh_availabilityimpact_NONE+cvssV3_BASE_score_0_iot_availabilityimpact_NONE)*100)/(cvssV3_BASE_score_0_sh+cvssV3_BASE_score_0_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
    print("\n")
    print("\n")
print("      -    EN EL "+str(float((((cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot)*100)/(len(df_cve_sh["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])+len(df_cve_iot["CVE_Items.impact.baseMetricV3.cvssV3.baseScore"])))))+" % DE  VULNERABILIDADES LA PUNTUACION BASE NO ESTÁ ESPECIFICADA. LOS PORCENTAJES DEL VECTOR CVSS3 SON LOS SIGUIENTES:  \n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_version_3_1+cvssV3_no_BASE_score_iot_version_3_1)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.1 ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_version_3_0+cvssV3_no_BASE_score_iot_version_3_0)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA VERSIÓN DEL VECTOR ES LA 3.0 ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackvector_NETWORK+cvssV3_no_BASE_score_iot_attackvector_NETWORK)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES NETWORK ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackvector_LOCAL+cvssV3_no_BASE_score_iot_attackvector_LOCAL)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES LOCAL ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackvector_PHYSICAL+cvssV3_no_BASE_score_iot_attackvector_PHYSICAL)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES PHYSICAL ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackvector_ADJACENT_NETWORK+cvssV3_no_BASE_score_iot_attackvector_ADJACENT_NETWORK)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL VECTOR DE ATAQUE ES ADJACENT_NETWORK ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackcomplexity_HIGH+cvssV3_no_BASE_score_iot_attackcomplexity_HIGH)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES ALTA ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackcomplexity_LOW+cvssV3_no_BASE_score_iot_attackcomplexity_LOW)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES BAJA ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackcomplexity_MEDIUM+cvssV3_no_BASE_score_iot_attackcomplexity_MEDIUM)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE ES MEDIA ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_attackcomplexity_NONE+cvssV3_no_BASE_score_iot_attackcomplexity_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES LA COMPLEJIDAD DE ATAQUE NO VIENE ESPECIFICADA ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_privilegesrequired_HIGH+cvssV3_no_BASE_score_iot_privilegesrequired_HIGH)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS ALTOS ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_privilegesrequired_LOW+cvssV3_no_BASE_score_iot_privilegesrequired_LOW)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS BAJOS")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_privilegesrequired_MEDIUM+cvssV3_no_BASE_score_iot_privilegesrequired_MEDIUM)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES SE REQUIEREN PRIVILEGIOS MEDIOS ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_privilegesrequired_NONE+cvssV3_no_BASE_score_iot_privilegesrequired_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES NO VIENEN ESPECIFICADAS SI SE REQUIEREN PRIVILEGIOS")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_userinteraction_REQUIRED+cvssV3_no_BASE_score_iot_userinteraction_REQUIRED)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES SE REQUIERE INTERACCIÓN DE USUARIO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_userinteraction_NONEREQUIRED+cvssV3_no_BASE_score_iot_userinteraction_NONEREQUIRED)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES NO SE REQUIERE INTERACCIÓN DE USUARIO")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_scope_CHANGED+cvssV3_no_BASE_score_iot_scope_CHANGED)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES CHANGED ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_scope_UNCHANGED+cvssV3_no_BASE_score_iot_scope_UNCHANGED)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL SCOPE ES UNCHANGED")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_scope_NONE+cvssV3_no_BASE_score_iot_scope_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL SCOPE NO VIENE ESPECIFICADO ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_confidentialityimpact_HIGH+cvssV3_no_BASE_score_iot_confidentialityimpact_HIGH)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_confidentialityimpact_LOW+cvssV3_no_BASE_score_iot_confidentialityimpact_LOW)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_confidentialityimpact_MEDIUM+cvssV3_no_BASE_score_iot_confidentialityimpact_MEDIUM)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE CONFIDENCIALIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_confidentialityimpact_NONE+cvssV3_no_BASE_score_iot_confidentialityimpact_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES NO SE PRODUCE NINGUN IMPACTO DE CONFIDENCIALIDAD ")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_integrityimpact_HIGH+cvssV3_no_BASE_score_iot_integrityimpact_HIGH)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_integrityimpact_LOW+cvssV3_no_BASE_score_iot_integrityimpact_LOW)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_integrityimpact_MEDIUM+cvssV3_no_BASE_score_iot_integrityimpact_MEDIUM)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE INTEGRIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_integrityimpact_NONE+cvssV3_no_BASE_score_iot_integrityimpact_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE INTEGRIDAD ")
print("\n")
print("\n")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_availabilityimpact_HIGH+cvssV3_no_BASE_score_iot_availabilityimpact_HIGH)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES ALTO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_availabilityimpact_LOW+cvssV3_no_BASE_score_iot_availabilityimpact_LOW)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES BAJO" )
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_availabilityimpact_MEDIUM+cvssV3_no_BASE_score_iot_availabilityimpact_MEDIUM)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES EL IMPACTO DE DISPONIBILIDAD ES MEDIO ")
print("            -    EN EL "+str(float((((cvssV3_no_BASE_score_sh_availabilityimpact_NONE+cvssV3_no_BASE_score_iot_availabilityimpact_NONE)*100)/(cvssV3_no_BASE_score_sh+cvssV3_no_BASE_score_iot))))+" % DE  VULNERABILIDADES NO SE SUFRE IMPACTO DE DISPONIBILIDAD ")
print("\n")
print("\n")




























     
                        
            
    
            
            
        
            


























































