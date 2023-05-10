# Funções selecionadas a partir do módulo random .
#
# A função random .
#
# A função mais geral chamada random() (não confundir com o nome do módulo) produz um número float x vindo do intervalo (0.0, 1.0) - por outras palavras: (0,0 <= x < 1,0).
#
# O programa de exemplo abaixo produzirá cinco valores pseudo-aleatórios - como os seus valores são determinados pelo valor atual (bastante imprevisível) da seed, não se pode adivinhá-los:
#
from random import random

print("Exemplo 01 - Imprimindo numeros aleatorios com o modulo random", end="")
for i in range(5):
    print(random())

# Execute o programa. Isto é o que obtivemos:
# 0.9535768927411208
# 0.5312710096244534
# 0.8737691983477731
# 0.5896799172452125
# 0.02116716297022092
#
# output de amostra
#
# A seed .
#
# A função seed() é capaz de definir diretamente a seed do gerador. Vamos mostrar-lhe duas das suas variantes:
#
#    seed() - define a seed com a hora atual;
#    seed(int_value) - define a seed com o valor inteiro int_value.0
#
# Modificámos o programa anterior - com efeito, removemos qualquer vestígio de aleatoriedade do código:

from random import random, seed

seed(0)

print()
print("Exemplo 01 - Imprimindo numeros aleatorios com o modulo random com seed", end="")
for i in range(5):
    print(random())


# Devido ao facto de a seed ser sempre definida com o mesmo valor, a sequência de valores gerados parece sempre a mesma.
#
# Execute o programa. Isto é o que obtivemos:
# 0.844421851525
# 0.75795440294
# 0.420571580831
# 0.258916750293
# 0.511274721369
#
# output de amostra
#
# E você?
# 
# Nota: os seus valores podem ser ligeiramente diferentes dos nossos se o seu sistema utilizar uma aritmética de floating-point mais ou menos precisa, mas a diferença será vista bastante longe do ponto 
# decimal.
