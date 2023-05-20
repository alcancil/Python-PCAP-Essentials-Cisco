# ImportError
#
# Localização: BaseException ← Exception ← StandardError ← ImportError
#
# Descrição: uma exceção concreta levantada quando uma operação de importação falha
#
# Código:
# One of these imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')



# KeyError
#
# Localização: baseException ← Exceção ← LookuPerror ← KeyError
#
# Descrição: uma exceção concreta levantada quando se tenta aceder ao elemento inexistente de uma coleção (por exemplo, o elemento de um dicionário)
#
# Código:
# How to abuse the dictionary
# and how to deal with it?

dictionary = { 'a': 'b', 'b': 'c', 'c': 'd' }
ch = 'a'

try:
    while True:
        ch = dictionary[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)


# Por agora acabámos com as exceções, mas voltarão quando discutirmos a programação orientada ao objeto em Python. Pode utilizá-las para proteger o seu código contra acidentes graves, mas também tem de 
# aprender a mergulhar nelas, explorando a informação que transportam.
#
# As exceções são de facto objetos - no entanto, nada podemos dizer sobre este aspeto até lhe apresentarmos classes, objetos, e afins.
#
# Por enquanto, se quiser saber mais sobre exceções por si próprio, consulte a Biblioteca Padrão Python em https://docs.python.org/3.6/library/exceptions.html.
