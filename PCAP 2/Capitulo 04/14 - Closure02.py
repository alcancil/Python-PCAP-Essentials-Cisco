# Um breve olhar sobre closures: continuação
#
# Um closure tem de ser invocado exatamente da mesma forma como foi declarado.
#
# No exemplo abaixo:
# def outer(par):
#    loc = par
#
#    def inner():
#        return loc
#    return inner
#
#
# var = 1
# fun = outer(var)
# print(fun())
#
#
# a função inner() é sem parâmetros, pelo que temos de a invocar sem argumentos.
#
# Agora veja o código no editor. É totalmente possível declarar um closure equipado com um número arbitrário de parâmetros, por exemplo, um, tal como a power() função.
#
# Isto significa que o closure não só faz uso do ambiente congelado, como também pode modificar o seu comportamento, utilizando valores retirados do exterior.
#
# Este exemplo mostra mais uma circunstância interessante - pode criar tantos closures quantos quiser usando um e o mesmo código. Isso é feito com uma função chamada make_closure(). Nota:
#
#    o primeiro closure obtido a partir de make_closure() define uma ferramenta que enquadra o seu argumento;
#    o segundo foi concebido para cubrir o argumento.
#
# É por isso que o código produz o seguinte output:
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
#
# output
#
# Realize os seus próprios testes.

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
