# Como usar lambdas e para quê?
#
# A parte mais interessante da utilização de lambdas surge quando se pode utilizá-los na sua forma pura - como partes anónimas de código destinadas a avaliar um resultado.
#
# Imagine que precisamos de uma função (vamos nomeá-la print_function) que imprime os valores de uma determinada (outra) função para um conjunto de argumentos selecionados.
#
# Queremos que print_function seja universal - deve aceitar um conjunto de argumentos colocados numa lista e uma função a ser avaliada, ambos como argumentos - não queremos codificar nada.
#
# Veja o exemplo no editor. Foi assim que implementámos a ideia.

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)



# Vamos analisá-la. A função print_function() toma dois parâmetros:
#
#    o primeiro, uma lista de argumentos para os quais queremos imprimir os resultados;
#    o segundo, uma função que deve ser invocada tantas vezes quanto o número de valores que são recolhidos dentro do primeiro parâmetro.
#
# Nota: também definimos uma função chamada poly() - esta é a função cujos valores vamos imprimir. O cálculo que a função realiza não é muito sofisticado - é o polinomial (daí o seu nome) de uma forma:
#
# f(x) = 2x2 - 4x + 2
#
# O nome da função é então passado para o print_function() juntamente com um conjunto de cinco argumentos diferentes - o conjunto é construído com uma cláusula de compreensão de lista.
#
# O código imprime as seguintes linhas:
# f(-2)=18
# f(-1)=8
# f(0)=2
# f(1)=0
# f(2)=2
#
# output
#
# Podemos evitar definir a função poly() , já que não a vamos utilizar mais do que uma vez? Sim, podemos - este é o benefício que uma lambda pode trazer.
#
# Veja o exemplo em baixo. Consegue ver a diferença?

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)


# A função print_function() permaneceu exatamente a mesma, mas não há nenhuma poly() função. Já não precisamos dela, pois o polinómio está agora diretamente dentro da invocação print_function() sob a forma # de um lambda definido da seguinte forma:
# 
# lambda x: 2 * x**2 - 4 * x + 2
#
# O código tornou-se mais curto, mais claro e mais legível.
#
# Deixe-nos mostrar-lhe outro lugar onde os lambdas podem ser úteis. Começaremos com uma descrição de map(), uma função integrada de Python. O seu nome não é demasiado descritivo, a sua ideia é simples, e a # função em si é realmente utilizável.