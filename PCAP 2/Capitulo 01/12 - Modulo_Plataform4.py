# Funções selecionadas a partir do módulo platform : continuação
#
# As funções system .
#
# Uma função chamada system() devolve o nome genérico do SO como uma cadeia.
#
# As nossas plataformas de exemplo apresentaram-se desta forma:
#
# Intel x86 + Windows Vista (32 bit):
# Windows
#
# output
#
# Intel x86 + Gentoo Linux (64 bits):
# Linux
#
# output
#
# Raspberry PI2+ Linux Raspbian (32 bits):
# Linux


from platform import system

print(system())
