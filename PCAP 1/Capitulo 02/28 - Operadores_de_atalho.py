# Operadores de atalho
# Chegou a hora do próximo conjunto de operadores que facilitam a vida de um programador.
#
# Muito frequentemente, queremos utilizar uma e a mesma variável tanto para o lado direito como para o esquerdo do = operador.
#
# Por exemplo, se precisarmos de calcular uma série de valores sucessivos de potências de 2, podemos utilizar uma peça como esta:
# 
# x = x * 2
#
# Pode usar uma expressão como esta se não conseguir adormecer e estiver a tentar lidar com ela usando alguns métodos bons e antiquados:
#
# sheep = sheep + 1
#
# O Python oferece-lhe uma forma abreviada de escrever operações como estas, que podem ser codificadas como se segue:
#
# x *= 2
# sheep += 1
#
# Vamos tentar apresentar uma descrição geral para estas operações.
#
# Se op é um operador de dois argumentos (esta é uma condição muito importante) e o operador é utilizado no seguinte contexto:
#
# variable = variable op expression
#
# Pode ser simplificado e mostrado da seguinte forma:
#
# variable op= expression
#
# Dê uma vista de olhos nos exemplos abaixo. Certifique-se de que os compreende a todos.
#
# i = i + 2 * j ⇒ i += 2 * j
#
# var = var / 2 ⇒ var /= 2
#
# rem = rem % 10 ⇒ rem %= 10
#
# j = j - (i + var + rem) ⇒ j -= (i + var + rem)
#
# x = x ** 2 ⇒ x **= 2

i = 1
i = i + 2
print(i)

i = 1
i += 2
print(i)