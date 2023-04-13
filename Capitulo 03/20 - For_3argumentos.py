# FOR
#
# O comando for é um Loop.
# A sua sintaxe é a seginte : For i in range (argumento01, argumento02)
#
# OBS: i é uma váriavel
#
# Os argumentos funcionam assim: o primeiro argumento é o inicio e o segundo é o final
# Ou seja, para i no intervalo de argumento01 até o argumento02
# OBS: o pyton inicia a contagem em 0. Se os argumentos forem de 1 a 10, por exemplo. O for vai até o número 9
# começando a contagem em 1
#
# Esse é o uso tradicional. Mas existem casos em que se pode querer utilizar 3 argumentos
#
# For i in range (argumento01, argumento02, argumento03) 
#
# Agora o argumento01 é o inicio. O argumento02 é o final do loop. Mas e o argumento 03 ?
# O argumento03 é o incremento, ou seja de quanto em quanto ele vai variar
#
# Exemplo:
#
for i in range(2, 18, 3):
    print("The value of i is currently", i)
#
#
# A saída será:
# The value of i is currently 2
# The value of i is currently 5
# The value of i is currently 8
# The value of i is currently 11
# The value of i is currently 14
# The value of i is currently 17
#
# Traduzindo, o código fala assim: para i de 2 a 18 variando de 3 em 3 faça: