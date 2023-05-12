# Operações em strings: o método list() .
#
# A função list() toma o seu argumento (uma string) e cria uma nova lista contendo todos os carateres da string, um por elemento de lista.
#
# Nota: não é estritamente uma função string - list() é capaz de criar uma nova lista de muitas outras entidades (por exemplo, de tuples e dicionários).
#
# Dê uma vista de olhos no exemplo de código no editor.
#
# O output do exemplo:
# ['a', 'b', 'c', 'a', 'b', 'c']
#
# output
# Operações em strings: o método count() .
#
# A classe count() conta todas as ocorrências do elemento dentro da sequência. A ausência de tais elementos não causa problemas.
#
# Veja o segundo exemplo no editor. Consegue adivinhar o seu output?
#
# É:
# 2
# 0
#
# output
#
# Além disso, as strings em Python têm um número significativo de métodos destinados exclusivamente ao processamento de carateres. Não espere que funcionem com quaisquer outras coleções. A lista completa é 
# apresentada aqui: https://docs.python.org/3.4/library/stdtypes.html#string-methods.
#
# Vamos mostrar-lhe as que consideramos mais úteis.

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))