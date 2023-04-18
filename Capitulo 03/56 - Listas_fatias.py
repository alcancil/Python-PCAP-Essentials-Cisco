# Slices poderosas
# Felizmente, a solução está ao seu alcance - o seu nome é slice.
#
# Uma slice é um elemento da sintaxe Python que lhe permite fazer uma cópia completamente nova de uma lista ou partes de uma lista.
#
# Na verdade, a slice copia o conteúdo da lista, não o seu nome.
#
# Isto é exatamente o que necessita. Dê uma vista de olhos no snippet em baixo:

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

#
# O seu output é [1].
#
# Esta parte inconspícua do código descrito como [:] é capaz de produzir uma lista completamente nova.
#
# Uma das formas mais gerais da slice tem o seguinte aspeto:
#
# my_list[start:end]
#
# Como pode ver, assemelha-se à indexação, mas os dois pontos no interior fazem uma grande diferença.
#
# Uma slice desta forma faz uma nova lista (alvo), retirando elementos da source list - os elementos dos índices desde o início até end - 1.
#
# Nota: não para end mas para end - 1. Um elemento com um índice igual a end é o primeiro elemento que não participa no slicing.
#
# É possível utilizar valores negativos tanto para o início como para o fim (tal como na indexação).
#
# Veja o snippet:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


# A new_list lista terá end - start (3 - 1 = 2) elementos - aqueles com índices iguais a 1 e 2 (mas não 3).
#
# O output do snippet é: [8, 6]

