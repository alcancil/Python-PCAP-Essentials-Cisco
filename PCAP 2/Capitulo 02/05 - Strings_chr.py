# Operações em strings: chr()
#
# Se conhece o code point (número) e pretende obter o caratere correspondente, pode utilizar uma função chamada chr().
#
# A função toma um code point e devolve o seu caratere.
#
# Invocá-lo com um argumento inválido (por exemplo, um code point negativo ou inválido) causa ValueError ou TypeError exceções.
#
# Execute o código no editor. O output do snippet de exemplo:
# a
# α
#
# output
#
# Nota:
#
#    chr(ord(x)) == x
#    ord(chr(x)) == x
#
# Mais uma vez, faça as suas próprias experiências.

# Demonstrating the chr() function.

print(chr(97))
print(chr(945))