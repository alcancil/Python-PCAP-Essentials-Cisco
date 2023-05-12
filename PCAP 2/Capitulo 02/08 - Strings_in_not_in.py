# Os loops Operadores in e not in .
#
# O operador in .
#
# O operador in não deve surpreendê-lo quando aplicado a strings - simplesmente verifica se o seu argumento esquerdo (uma string) pode ser encontrado em qualquer lugar dentro do argumento direito (outra 
# string).
#
# O resultado da verificação é simplesmente True ou False.
#
# Veja o programa de exemplo abaixo. É assim que o operador in funciona:

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)


# O output do exemplo é:
# True
# False
# False
# True
# False
#
# output
#
# O método not in .
#
# Como provavelmente suspeita, o operador not in também é aplicável aqui.
#
# É assim que funciona:
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


# O output do exemplo é:
# False
# True
# True
# False
# True

