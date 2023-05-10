# Funções selecionadas a partir do módulo random : continuação
#
# As funções anteriores têm uma desvantagem importante - podem produzir valores repetitivos mesmo que o número de invocações subsequentes não seja maior do que a largura do intervalo especificado.
#
# Veja o código abaixo - o programa produz muito provavelmente um conjunto de números em que alguns elementos não são únicos:

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')


# Isto é o que obtivemos num dos lançamentos:
# 9,4,5,4,5,8,9,4,8,4,
#
# output de amostra
#
# A choice e sample funções
#
# Como pode ver, esta não é uma boa ferramenta para gerar números numa lotaria. Felizmente, existe uma solução melhor do que escrever o seu próprio código para verificar a singularidade dos números 
# "sorteados".
#
# É uma função chamada de uma maneira muito sugestiva - choice:
# 
#    choice(sequence)
#    sample(sequence, elements_to_choose)
#
# A primeira variante escolhe um elemento "aleatório" a partir da sequência de input e devolve-o.
#
# O segundo constrói uma lista (uma amostra; em inglês, uma sample) que consiste no elemento elements_to_choose “sorteado” a partir da sequência de input.
#
# Por outras palavras, a função escolhe (em inglês, chooses) alguns dos elementos de input, devolvendo uma lista com a escolha. Os elementos da amostra são colocados em ordem aleatória. Nota: o 
# elements_to_choose não deve ser maior do que o comprimento da sequência de input.
#
# Veja o código abaixo:
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

#
# Novamente, o output do programa não é previsível. Os nossos resultados foram os seguintes:
# 4
# [3, 1, 8, 9, 10]
# [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]

