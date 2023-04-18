# Listas em ação
# Agora pode facilmente trocar os elementos da lista para inverter a sua ordem:
#
# my_list = [10, 1, 8, 3, 5]
#
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
#
# print(my_list)
#
#
# Execute o snippet. O seu output deve ter este aspeto:
#
# [5, 3, 8, 1, 10]
# output
#
#
# Fica bem com cinco elementos.
#
#
# Será ainda aceitável com uma lista contendo 100 elementos? Não, não será.
#
# Pode utilizar o loop for para fazer a mesma coisa automaticamente, independentemente do comprimento da # lista? Sim, pode.
#
# Foi assim que o fizemos:
#
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


# Nota:
#
# nós atribuímos a variável length com o comprimento da lista atual (isto torna o nosso código um pouco # mais claro e mais curto)
# lançámos o loop for para correr através do seu corpo length // 2 vezes (isto funciona bem para listas # com comprimentos pares e ímpares, porque quando a lista contém um número ímpar de elementos, o do meio # permanece intocado)
# trocamos o i-ésimo elemento (desde o início da lista) com o que tem um index igual a (length - i - 1) # (do final da lista); no nosso exemplo, para i igual a 0 o ramo (lenght - i - 1) dá 4; para i igual a 
# 1, dá 3 - Isto é exatamente o que precisávamos.
# As listas são extremamente úteis, e irá encontrá-las com muita frequência.

