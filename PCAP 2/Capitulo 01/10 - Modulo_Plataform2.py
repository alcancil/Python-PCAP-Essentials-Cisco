# Funções selecionadas a partir do módulo platform : continuação
#
# As funções machine .
#
# Por vezes, pode apenas querer saber o nome genérico do processador que executa o seu SO juntamente com o Python e o seu código - uma função chamada machine() dir-lhe-á isso. Como anteriormente, a função 
# devolve uma string.
#
# Mais uma vez, executámos o programa de amostra em três plataformas diferentes:
#
# Intel x86 + Windows Vista (32 bit):
# x86
#
# output
#
# Intel x86 + Gentoo Linux (64 bits):
# x86_64
#
# output
#
# Raspberry PI2+ Linux Raspbian (32 bits):
# armv7l


from platform import machine

print(machine())

