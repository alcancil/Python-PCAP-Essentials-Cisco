# Variáveis de instância: continuação
#
# Dê uma vista de olhos ao exemplo modificado no editor.
#
# É quase o mesmo que o anterior. A única diferença está nos nomes das propriedades. Adicionámos dois underscores (__) à frente deles.
#
# Como sabe, tal adição torna a variável de instância privada - torna-se inacessível a partir do mundo exterior.
#
# O comportamento real destes nomes é um pouco mais complicado, por isso vamos executar o programa. Este é o output:
# {'_ExampleClass__first': 1}
# {'_ExampleClass__first': 2, '_ExampleClass__second': 3}
# {'_ExampleClass__first': 4, '__third': 5}
#
# output
#
# Consegue ver estes estranhos nomes cheios de underscores? De onde vieram eles?
#
# Quando o Python vê que quer adicionar uma variável de instância a um objeto, e vai fazê-lo dentro de qualquer um dos métodos do objeto, ele modula a operação da seguinte forma:
#
#    coloca um nome de classe antes do seu nome;
#    coloca um underscore adicional no início.
#
# É por isso que o __first torna-se _ExampleClass__first.
#
# O nome é agora totalmente acessível a partir do exterior da classe. Pode executar um código como este:
# print(example_object_1._ExampleClass__first)
#
#
# e obterá um resultado válido, sem erros ou exceções.
#
# Como pode ver, tornar uma propriedade privada é limitado.
#
# O mangling não funcionará se se adicionar uma variável de instância privada fora do código de classe. Neste caso, comportar-se-á como qualquer outra propriedade.

class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


print(example_object_1._ExampleClass__first)