# Exceções integradas
#
# Vamos mostrar-lhe uma pequena lista das exceções mais úteis. Embora possa parecer estranho chamar "útil" a uma coisa ou fenómeno que é um sinal visível de fracasso ou contratempo, como sabe, errar é 
# humano, e se algo pode correr mal, correrá mal.
#
# As exceções são tão rotineiras e normais como qualquer outro aspeto da vida de um programador.
#
# Para cada exceção, mostraremos:
#
#    o seu nome;
#    a sua localização na árvore de exceção;
#    uma breve descrição;
#    um snippet conciso de código mostrando as circunstâncias em que a exceção pode ser levantada.
#
# Há muitas outras exceções a explorar - simplesmente não temos espaço para as explorar todas.
# ArithmeticError
#
# Localização: BaseException ← Exception ← ArithmeticError
#
# Descrição: uma exceção abstrata incluindo todas as exceções causadas por operações aritméticas como a divisão zero ou o domínio inválido de um argumento
# AssertionError
#
# Localização: BaseException ← Exception ← AssertionError
#
# Descrição: uma exceção concreta levantada pela instrução assert quando a sua argumentação avalia para False, None, 0, ou uma string vazia
#
# Código:
# from math import tan, radians
# angle = int(input('Enter integral angle in degrees: '))
#
# We must be sure that angle != 90 + k * 180
# assert angle % 180 != 90
# print(tan(radians(angle)))
#
#
#
# BaseException
#
# Localização: BaseException
#
# Descrição: mais geral (abstrata) de todas as exceções Python - todas as outras exceções estão incluídas nesta; pode dizer-se que os doss seguintes except ramos são equivalentes: except: e except 
# BaseException:.
# IndexError
#
# Localização: BaseException ← Exception ← LookupError ← IndexError
#
# Descrição: uma exceção concreta levantada quando se tenta aceder a um elemento de uma sequência inexistente (por exemplo, o elemento de uma lista)
#
# Código:
# The code shows an extravagant way
# of leaving the loop.

the_list = [1, 2, 3, 4, 5]
ix = 0
do_it = True

while do_it:
    try:
        print(the_list[ix])
        ix += 1
    except IndexError:
        do_it = False

print('Done')



