# A vida interior das classes e objetos: continuação
#
# __bases__ é um tuple. O tuple contém classes (não nomes de classe) que são superclasses diretas para a classe.
#
# A ordem é a mesma que é utilizada dentro da definição de classe.
#
# Mostrar-lhe-emos apenas um exemplo muito básico, uma vez que queremos destacar como funciona a herança.
#
# Além disso, vamos mostrar-lhe como utilizar este atributo quando discutirmos os aspetos objetivos das exceções.
#
# Nota: apenas as classes têm este atributo - os objetos não o têm.
#
# Definimos uma função chamada printbases(), concebida para apresentar claramente o conteúdo do tuple.
#
# Veja o código no editor. Analise e execute-o. Ele terá como output:
# ( object )
# ( object )
# ( SuperOne SuperTwo )
#
# output
#
# Nota: uma classe sem superclasses explícitas aponta para o objeto (uma classe Python predefinida) como seu antepassado direto.


class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
