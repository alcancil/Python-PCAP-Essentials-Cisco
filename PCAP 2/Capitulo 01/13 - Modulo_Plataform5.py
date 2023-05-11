# Funções selecionadas a partir do módulo platform : continuação
#
# As funções version função
#
# A versão do SO é fornecida como uma string pela version() função.
#
# Execute o código e verifique o seu output. Isto é o que obtivemos:
#
# Intel x86 + Windows Vista (32 bit):
# 6.0.6002
#
# output
#
# Intel x86 + Gentoo Linux (64 bits):
# #1 SMP PREEMPT Fri Jul 21 22:44:37 CEST 2017
#
# output
#
# Raspberry PI2+ Linux Raspbian (32 bits):
# #1 SMP Debian 4.4.6-1+rpi14 (2016-05-05)


from platform import version

print(version())
