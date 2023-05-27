# Como construir o seu próprio gerador
#
# E se precisar de um gerador para produzir as primeiras n potências de 2?
#
# Nada mais fácil. Basta olhar para o código abaixo:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)


# Consegue adivinhar o output? Copie o código para o editor e execute-o para verificar os seus palpites.
#
# Compreensões de lista
#
# Os geradores também podem ser utilizados no âmbito das compreensões de lista, tal como aqui:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = [x for x in powers_of_2(5)]
print(t)


# Execute o exemplo e verifique o output.
#
# A list() .
#
# A função list() pode transformar uma série de invocações de geradores subsequentes numa lista real:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)


# Mais uma vez, tente prever o output e execute o código para verificar as suas previsões.
#
# O operador in .
#
# Além disso, o contexto criado pelo operador in também permite a utilização de um gerador.
#
# O exemplo mostra como o fazer:

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for i in range(20):
    if i in powers_of_2(4):
        print(i)


# Qual é o output do código? Execute o programa e verifique.
#
# O gerador de números Fibonacci
#
# Agora vamos ver um gerador de números Fibonacci, e assegurar que tenha muito melhor aspeto do que a versão objetiva baseada na implementação do protocolo de iterador direto.
#
# Aqui está:

def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)


# Adivinhe o output (uma lista) produzida pelo gerador, e execute o código para verificar se estava certo.