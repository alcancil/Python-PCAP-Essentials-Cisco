# Strings como sequências: indexação
#
# Dissemos-lhe antes que as strings de Python são sequências. É tempo de lhe mostrar o que isso realmente significa.
#
# As strings não são listas, mas pode tratá-las como listas em muitos casos particulares.
#
# Por exemplo, se quiser aceder a qualquer um dos carateres de uma string, pode fazê-lo utilizando a indexação, tal como no exemplo abaixo. Execute o programa:
# 
# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


# Tenha cuidado - não tente passar os limites de uma string - isso causará uma exceção.
#
# O output do exemplo é:
# s i l l y   w a l k s
#
# output
#
# A propósito, os índices negativos também se comportam como esperado. Verifique isto você mesmo.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[-ix], end=' ')

print()


# Strings como sequências: iteração
#
# Iterar através das strings também funciona. Veja o exemplo abaixo:
# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# O output é o mesmo que anteriormente. Verifique.