# A vida interior das classes e objetos: continuação
#
# __dict__ é um dicionário. Outra propriedade integrada que vale a pena mencionar é __name__, que é uma string.
#
# A propriedade contém o nome da classe Não é nada de excitante, apenas uma cadeia.
#
# Nota: o atributo __name__ está ausente do objeto - só existe dentro das classes.
#
# Se quiser encontrar a classe de um determinado objeto, pode usar uma função chamada type(), que é capaz (entre outras coisas) de encontrar uma classe que tenha sido utilizada para instanciar qualquer 
# objeto.
#
# Olhe para o código no editor, execute-o, e veja por si mesmo.
#
# Output do código:
# Classy
# Classy
#
# output
#
# Observe que uma declaração como esta:
# print(obj.__name__)
#
#
# irá causar um erro.


class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)