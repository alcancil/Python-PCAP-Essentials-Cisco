# Comparar strings: continuação
#
# Mesmo que uma string contenha apenas dígitos, ainda assim não é um número. É interpretada como qualquer outra string regular, e o seu (potencial) aspeto numérico não é tomado em consideração de forma 
# alguma.
#
# Veja os exemplos:
# '10' == '010'
# '10' > '010'
# '10' > '8'
# '20' < '8'
# '20' < '80'
#
#
# Eles produzem os seguintes resultados:
# False
# True
# False
# True
# True
# 
# output
#
# Comparar strings com números é geralmente uma má ideia.
#
# As únicas comparações que pode efetuar com impunidade são estas simbolizadas pelos == e != . O primeiro dá sempre False, enquanto o último produz sempre True.
#
# A utilização de qualquer um dos restantes operadores de comparação irá levantar uma TypeError exceção.
# 
# Verifiquemos:
# '10' == 10
# '10' != 10
# '10' == 1
# '10' != 1
# '10' > 10
#
#
# Os resultados neste caso são:
# False
# True
# False
# True
# TypeError exception
#
# output
# 
# Execute todos os exemplos, e realize mais experiências