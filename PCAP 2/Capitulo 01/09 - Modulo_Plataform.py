# Funções selecionadas a partir do módulo platform .
#
# A função platform .
#
# A função platform permite-lhe aceder aos dados da plataforma subjacente, ou seja, hardware, sistema operativo, e informação da versão do intérprete.
#
# Existe uma função que lhe pode mostrar todas as camadas subjacentes num só relance, denominada platform, também. Apenas devolve uma string descrevendo o ambiente; assim, o seu output é mais dirigido ao ser # humano do que ao processamento automatizado (vê-lo-á em breve).
#
# É assim que pode invocá-la:
#
# platform(aliased = False, terse = False)
#
# E agora:
#
#    aliased → quando definido para True (ou qualquer valor não nulo) pode fazer com que a função apresente os nomes alternativos das camadas subjacentes em vez dos nomes comuns;
#    terse → quando definido para True (ou qualquer valor não nulo) pode convencer a função a apresentar uma forma mais breve do resultado (se possível)
#
# Executámos o nosso programa de amostra utilizando três plataformas diferentes - isto é o que obtivemos:
#
# Intel x86 + Windows Vista (32 bit):
# Windows-Vista-6.0.6002-SP2
# Windows-Vista-6.0.6002-SP2
# Windows-Vista
#
# output
#
# Intel x86 + Gentoo Linux (64 bits):
# Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
# Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-gentoo-2.3
# Linux-3.18.62-g6-x86_64-Intel-R-_Core-TM-_i3-2330M_CPU_@_2.20GHz-with-glibc2.3.4
#
# output
#
# Raspberry PI2+ Linux Raspbian (32 bits):
# Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
# Linux-4.4.0-1-rpi2-armv7l-with-debian-9.0
# Linux-4.4.0-1-rpi2-armv7l-with-glibc2.9
#
# output
#
# Também pode executar o programa de amostra em IDLE na sua máquina local para verificar qual o output que terá.
#
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))
