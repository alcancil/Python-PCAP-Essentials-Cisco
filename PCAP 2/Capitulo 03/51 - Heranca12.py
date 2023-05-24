# Como o Python encontra propriedades e métodos: continuação
#
# Vamos analisar o exemplo no editor.
#
# Ambas as classes Level1 e Level2 definem um método chamado fun() e uma propriedade chamada var. Isto significa que o objecto de classe Level3 poderá ter acesso a duas cópias de cada entidade? De modo algum.
#
# A entidade definida mais tarde (no sentido da herança) sobrepõe-se à mesma entidade definida mais cedo. É por isso que o código produz o seguinte output:
# 200 201
#
# output
#
# Como pode ver, o argumento de keyword var e método fun() a partir da classe Level2 substituem as entidades com os mesmos nomes derivados da classe Level1 .
#
# Esta característica pode ser intencionalmente utilizada para modificar comportamentos padrão (ou previamente definidos) de classe quando qualquer uma das suas classes precisa de agir de uma forma diferente # da dos seus antepassados.
#
# Podemos também dizer que o Python procura uma entidade de baixo para cima, e está plenamente satisfeito com a primeira entidade do nome desejado.
#
# Como funciona quando uma classe tem dois antepassados que oferecem a mesma entidade, e eles estão no mesmo nível? Por outras palavras, o que se deve esperar quando uma classe emerge usando herança múltipla? # Vamos ver isto.

class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())
