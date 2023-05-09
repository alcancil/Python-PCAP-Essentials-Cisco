# Replicação
# O sinal * (asterisco), quando aplicado a uma string e número (ou um número e string, visto permanecer comutativo nesta posição) torna-se um operador # de replicação:
#
# string * number
# number * string
#
# 
# Replica a string o mesmo número de vezes especificado pelo número.
#
# Por exemplo:
#
# "James" * 3 dá "JamesJamesJames"
# 3 * "an" dá "ananan"
# 5 * "2" (ou "2" * 5) dá "22222" (não 10!)
#
# LEMBRE-SE
#
# Um número menor ou igual a zero produz uma string vazia.
#
#
# Este programa simples "desenha" um retângulo, fazendo uso de um antigo operador (+) num novo papel:
#
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
#
#
# Note a forma como utilizámos os parêntesis na segunda linha do código.
#
# Tente praticar para criar outras formas ou a sua própria obra de arte!
#
#
print("╔" + 100 * "═" + "╗")
print(("║" + 100 * " " + "║") , end=" \n")
print(("║" + 100 * " " + "║") , end=" \n")
print(("║" + 100 * " " + "║") , end=" \n")
print(("║" + 100 * " " + "║") , end=" \n")
print("╚" + 100 * "═" + "╝"