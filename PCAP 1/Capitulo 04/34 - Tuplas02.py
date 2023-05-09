# Como usar um tuple: continuação
#
# Que mais podem os tuples fazer por si?
#
#    a função len() aceita tuples, e devolve o número de elementos contidos no seu interior;
#    o operador + pode juntar tuples (já lhe mostrámos isto)
#    o operador * pode multiplicar tuples, assim como listas;
#    os operadores in e not in trabalham da mesma maneira que nas listas.
#
# O snippet no editor apresenta-os a todos.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# O output deve ter a seguinte aparência:
# 9
# (1, 10, 100, 1000, 10000)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)
# True
# True
#
# output
#
# Uma das propriedades mais úteis da tuple é a sua capacidade de aparecer no lado esquerdo do operador de atribuição. Viu este fenómeno há algum tempo, quando foi necessário encontrar uma ferramenta 
# elegante para trocar os valores de duas variáveis.
#
# Dê uma vista de olhos no snippet abaixo:
var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)
#
#
# Mostra três tuples que interagem - com efeito, os valores neles armazenados "circulam" - t1 torna-se t2, t2 torna-se t3, e t3 torna-se t1.
#
# Nota: o exemplo apresenta mais um facto importante: os elementos de um tuple podem ser variáveis, e não apenas literais. Além disso, podem ser expressões se estiverem no lado direito do operador de 
# atribuição.