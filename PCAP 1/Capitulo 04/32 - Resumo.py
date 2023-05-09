
# Key takeaways
#
# 1. Uma função pode chamar outras funções ou até a ela própria. Quando uma função se chama a si própria, esta situação é conhecida como recursividade, e a função que se chama a si própria e contém uma 
# condição de terminação especificada (ou seja, o caso base - uma condição que não diz à função para fazer mais chamadas para essa função) é chamada de função recursiva.
#
# 2. Pode usar funções recursivas em Python para escrever um código limpo e elegante, e dividi-lo em pedaços mais pequenos e organizados. Por outro lado, é preciso ter muito cuidado, pois pode ser fácil 
# cometer um erro e criar uma função que nunca termina. Também é preciso lembrar que as chamadas recursivas consomem muita memória, e por isso podem por vezes ser ineficientes.
#
# Ao utilizar a recursividade, é necessário ter em consideração todas as suas vantagens e desvantagens.
#
# A função factorial é um exemplo clássico de como o conceito de recursividade pode ser posto em prática:
#
# Recursive implementation of the factorial function.

def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24





# Exercício 1
#
# O que acontecerá quando se tentar executar o seguinte snippet e porquê?
# def factorial(n):
#    return n * factorial(n - 1)
#
#
# print(factorial(4))
#
#
# A função factorial não tem condição de terminação (sem caso base), pelo que o Python irá levantar uma exceção (RecursionError: maximum recursion depth exceeded)
#
# Exercício 2
#
# Qual é o output do seguinte snippet?
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))
print(fun(30))


# output 56
