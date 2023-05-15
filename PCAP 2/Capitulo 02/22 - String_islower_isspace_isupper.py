# Os loops islower() .
#
# A classe islower() é uma variante picuinhas do isalpha() - aceita apenas letras minúsculas.
#
# Veja o Exemplo 1 no editor - o seu output é:
# False
# True
#
# output
#
# O método isspace() .
#
# A classe isspace() identifica apenas os espaços em branco - ignora qualquer outro caratere (o resultado é False então).
#
# Veja o Exemplo 2 no editor - o seu output é:
# True
# True
# False
#
# output
#
# O método isupper() .
#
# A classe isupper() é a versão maiúscula do islower() - concentra-se apenas em letras maiúsculas.
#
# Novamente, veja o Exemplo 3 no editor - o seu output é:
# False
# False
# True
#
# output
#
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())