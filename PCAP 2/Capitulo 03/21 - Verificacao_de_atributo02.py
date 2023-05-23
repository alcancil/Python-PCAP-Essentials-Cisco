# Verificação da existência de um atributo: continuação
#
# A instrução try-except dá-lhe a oportunidade de evitar problemas com propriedades inexistentes.
# 
# É fácil - veja o código no editor.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

try:
    print(example_object.b)
except AttributeError:
    pass


# Como se pode ver, esta ação não é muito sofisticada. Essencialmente, apenas varremos o problema para debaixo do tapete.
#
# Felizmente, há mais uma forma de lidar com o problema.
#
# O Python fornece uma função capaz de verificar com segurança se algum objeto/classe contém uma propriedade especificada. A função é chamada hasattr, e espera que lhe sejam transmitidos dois argumentos:
#
#    A classe ou o objeto a ser verificado;
#    o nome da propriedade cuja existência tem de ser comunicada (nota: tem de ser uma string contendo o nome do atributo, e não apenas o nome)
#
# A função devolve True ou False.
#
# É assim que a pode utilizar:

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)
print(example_object.a)

if hasattr(example_object, 'b'):
    print(example_object.b)

