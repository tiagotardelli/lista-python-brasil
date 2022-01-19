import math


populacao_pais_a = 80_000
taxa_crescimento_anual_a = 1.03
populacao_pais_b = 200_000
taxa_crescimento_anual_b = 1.015
anos_crescimento_a_passar_b = 0
while populacao_pais_a < populacao_pais_b:
    anos_crescimento_a_passar_b += 1
    populacao_pais_a = math.floor(populacao_pais_a * taxa_crescimento_anual_a)
    populacao_pais_b = math.floor(populacao_pais_b * taxa_crescimento_anual_b)
print(
f"""Levarão {anos_crescimento_a_passar_b} anos
Para A chegar a {populacao_pais_a}
Para B chegar a {populacao_pais_b}""")
