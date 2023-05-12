# As strings de Python são imutáveis
#
# Também lhe dissemos que as strings de Python são imutáveis. Esta é uma característica muito importante. O que significa isto?
#
# Isto significa principalmente que a semelhança de strings e listas é limitada. Nem tudo o que se pode fazer com uma lista pode ser feito com uma string.
#
# A primeira diferença importante não lhe permite utilizar a instrução del para remover qualquer coisa de uma string.
#
# O exemplo aqui não vai funcionar:
alphabet = "abcdefghijklmnopqrstuvwxyz"
del alphabet[0]
#
#
# A única coisa que pode fazer com del e uma string é remover a string como um todo. Tente fazê-lo.
#
# As strings de Python não têm o método append() - não se pode expandi-las de forma alguma.
#
# O exemplo abaixo está errado:
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.append("A")


# com a ausência do método append() , o método insert() é ilegal, também:
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet.insert(0, "A")