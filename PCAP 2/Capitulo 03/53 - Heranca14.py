# Como construir uma hierarquia de classes
#
# A construção de uma hierarquia de classes não é apenas arte por causa da arte.
#
# Se dividir um problema entre classes e decidir qual delas deve ser localizada no topo e qual deve ser colocada na base da hierarquia, tem de analisar cuidadosamente a questão, mas antes de lhe mostrarmos # como o fazer (e como não o fazer), queremos destacar um efeito interessante. Não é nada de extraordinário (é apenas uma consequência das regras gerais apresentadas anteriormente), mas lembrá-la pode ser 
# fundamental para compreender como funcionam alguns códigos, e como o efeito pode ser utilizado para construir um conjunto flexível de classes.
#
# Dê uma vista de olhos ao código no editor. Vamos analisá-lo:
#
#    existem duas classes, nomeadas One e Two, enquanto Two é derivada de One. Nada de especial. No entanto, uma coisa parece notável - o método do_it() .
#    o método do_it()é definido duas vezes: originalmente dentro One e subsequentemente dentro Two. A essência do exemplo reside no facto de ser invocado apenas uma vez - no interior One.
#
# A questão é - qual dos dois métodos será invocado pelas duas últimas linhas do código?
#
# A primeira invocação parece ser simples, e é simples, na verdade - invocando doanything() a partir do objeto chamado one irá obviamente ativar o primeiro dos métodos.
#
# A segunda invocação precisa de alguma atenção. Também é simples, se tivermos em mente como o Python encontra componentes de classe. A segunda invocação irá lançar do_it() na forma existente dentro da 
# classe Two , independentemente do facto de a invocação ter lugar dentro da classe One .
#
# Com efeito, o código produz o seguinte output:
# do_it from One
# do_it from Two
#
# output
#
# Nota: a situação em que a subclasse é capaz de modificar o seu comportamento de superclasse (tal como no exemplo) é chamada polimorfismo. A palavra vem do grego (polys: "muitas" e morphe, "forma"), o que # significa que uma e a mesma classe pode tomar várias formas dependendo das redefinições feitas por qualquer uma das suas subclasses.
#
# O método, redefinido em qualquer uma das superclasses, alterando assim o comportamento da superclasse, é chamado virtual.
#
# Por outras palavras, nenhuma classe é dada de uma vez por todas. O comportamento de cada classe pode ser modificado em qualquer altura por qualquer uma das suas subclasses.
#
# Vamos mostrar-lhe como usar o polimorfismo para alargar a flexibilidade de classe.

class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()
