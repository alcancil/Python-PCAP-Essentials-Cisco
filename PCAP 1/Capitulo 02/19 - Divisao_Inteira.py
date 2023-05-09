# Operadores aritméticos: divisão inteira
# Um sinal // (dupla barra) é um operador de divisão inteira. Difere do operador padrão / em dois detalhes:
# 
# o seu resultado não tem a parte fracionada - está ausente (para inteiros), ou é sempre igual a zero (para floats); isto significa que os resultados 
# são sempre arredondados;
# está em conformidade com a regra inteiro vs. float.
# Execute o exemplo abaixo e veja os resultados:
#
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
#
#
# Como se pode ver, a divisão inteiro por inteiro dá um resultado inteiro. Todos os outros casos produzem floats.
#
#
# Vamos fazer alguns testes mais avançados.
# 
# Veja o seguinte snippet:
#
print(6 // 4)
print(6. // 4)
#
#
# Imagine que usámos / em vez de // - consegue prever os resultados?
#
# Sim, seria 1.5 em ambos os casos. Isso é claro.
#
# Mas que resultados devemos esperar com // divisão?
#
# Execute o código e veja por si mesmo.
#
# O que obtemos são dois uns - um inteiro e um float.
#
# O resultado da divisão inteira é sempre arredondado para o valor inteiro mais próximo, que é inferior ao resultado real (não arredondado).
#
# Isto é muito importante: o arredondamento vai sempre para o número inteiro menor.
#
# Veja o código abaixo e tente prever os resultados mais uma vez:
#
print(-6 // 4)
print(6. // -4)
#
# Nota: alguns dos valores são negativos. Isto irá obviamente afetar o resultado. Mas como?
#
# O resultado são dois dois negativos. O resultado real (não arredondado) é -1.5 em ambos os casos. No entanto, os resultados são sujeitos a 
# arredondamento. O arredondamento vai para o menor valor inteiro, e o menor valor inteiro é -2, logo: -2 e -2.0.
#
# NOTA
#
# A divisão inteira também pode ser chamada floor division. Definitivamente, no futuro, deparar-se-á com este termo.