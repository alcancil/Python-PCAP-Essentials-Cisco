# Funções selecionadas a partir do módulo platform : continuação
# 
# As funções processor .
#
# A função processor() devolve uma string preenchida com o nome do processador real (se possível).
#
# Mais uma vez, executámos o programa de amostra em três plataformas diferentes:
# 
# Intel x86 + Windows Vista (32 bit):
# x86
# 
# output
#
# Intel x86 + Gentoo Linux (64 bits):
# Intel(R) Core(TM) i3-2330M CPU @ 2.20GHz
#
# output
#
# Raspberry PI2+ Linux Raspbian (32 bits):
# armv7l
#
# output
#
# Teste isto na sua máquina local.

from platform import processor

print(processor())