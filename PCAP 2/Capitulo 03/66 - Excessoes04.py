# Exceções são classes
#
# Todas as exceções Python integradas formam uma hierarquia de classes. Não há qualquer obstáculo à sua extensão se a considerar razoável.
#
# Veja o código no editor.
#
# Este programa descarta todas as classes de exceção pré-definidas sob a forma de uma impressão em forma de árvore.
#
# Como uma árvore é um exemplo perfeito de uma estrutura de dados recursiva, uma recursividade parece ser a melhor ferramenta para a atravessar. A função print_exception_tree() toma dois argumentos:
#
#    um ponto dentro da árvore a partir do qual começamos a atravessar a árvore;
#    um nível de nesting (vamos utilizá-lo para construir um desenho simplificado dos ramos da árvore)
#
# Comecemos pela raiz da árvore - a raiz das classes de exceção de Python é a classe BaseException (é uma superclasse de todas as outras exceções).
#
# Para cada uma das classes encontradas, realize o mesmo conjunto de operações:
#
#    imprimir o seu nome, retirado da propriedade __name__ ;
#    iterar através da lista de subclasses entregue pelo método __subclasses__() , e invocar recursivamente a função print_exception_tree() , incrementando o nível de nesting respetivamente.
#
#    Note-se como desenhámos os ramos e as bifurcações. A impressão não é classificada de forma alguma - pode tentar classificá-la você mesmo, se quiser um desafio. Além disso, existem algumas imprecisões 
# subtis na forma como alguns ramos são apresentados. Isso também pode ser corrigido, se assim o desejar.

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
   

