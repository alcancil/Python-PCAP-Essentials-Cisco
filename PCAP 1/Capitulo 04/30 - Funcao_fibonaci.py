# Algumas funções simples: números de Fibonacci
#
# Está familiarizado com os números de Fibonacci?
#
# São uma sequência de números inteiros construída usando uma regra muito simples:
#
#    o primeiro elemento da sequência é igual a um (Fib1 = 1)
#    o segundo também é igual a um (Fib2 = 1)
#    cada número subsequente é a soma dos dois números anteriores:
#    (Fibi = Fibi-1 + Fibi-2)
#
# Aqui estão alguns dos primeiros números de Fibonacci:
#
# fib_1 = 1
# fib_2 = 1
# fib_3 = 1 + 1 = 2
# fib_4 = 1 + 2 = 3
# fib_5 = 2 + 3 = 5
# fib_6 = 3 + 5 = 8
# fib_7 = 5 + 8 = 13
#
# O que pensa da implementação disto como uma função?
#
# Vamos criar a nossa função fib e testá-la. Aqui está:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))


# Analise o corpo do loop for cuidadosamente, e descubra como movemos as elem_1 e elem_2 variáveis através dos números de Fibonacci subsequentes.
#
# A parte de teste do código produz o seguinte output:
# 1 -> 1
# 2 -> 1
# 3 -> 2
# 4 -> 3
# 5 -> 5
# 6 -> 8
# 7 -> 13
# 8 -> 21
# 9 -> 34