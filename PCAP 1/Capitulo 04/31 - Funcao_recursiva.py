# Algumas funções simples: recursividade
#
# Há mais uma coisa que queremos mostrar-lhe para tornar tudo completo - é a recursividade.
#
# Este termo pode descrever muitos conceitos diferentes, mas um deles é especialmente interessante - o que se refere à programação informática.
#
# Neste campo, a recursividade é uma técnica em que uma função se invoca a si própria.
#
# Estes dois casos parecem ser os melhores para ilustrar o fenómeno - os números fatorials e Fibonacci. Especialmente o último.
#
# A definição dos números Fibonacci é um exemplo claro de recursividade. Já lhe dissemos isso:
#
# Fibi = Fibi-1 + Fibi-2
# 
# A definição do número i-th refere-se ao número i-1, e assim por diante, até se chegar aos dois primeiros.
#
# Pode ser usado no código? Sim, pode. Pode também tornar o código mais curto e claro.
#
# A segunda versão da nossa função fib() faz uso direto desta definição:
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


# O código é agora muito mais claro.
#
# Mas é realmente seguro? Isto implica algum risco?
#
# Sim, há de facto um pequeno risco. Se se esquecer de considerar as condições que podem parar a cadeia de invocações recursivas, o programa pode entrar num loop infinito. É preciso ter cuidado.
#
# O fatorial tem também um segundo lado recursivo. Veja:
#
# n! = 1 × 2 × 3 ×... × n-1 × n
#
# É óbvio que:
#
# 1 × 2 × 3 ×... × n-1 = (n-1)!
#
# Então, finalmente, o resultado é:
#
# n! = (n-1)! × n
#
# De facto, esta é uma receita pronta para a nossa nova solução.
#
# Aqui está:
def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)


# Funciona? Sim, funciona. Experimente você mesmo.
#
# A nossa curta viagem funcional está quase no fim. A secção seguinte tratará de dois curiosos tipos de dados Python: tuples e dicionários.

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


for n in range(1, 10):
    print(n, "->", fib(n))
