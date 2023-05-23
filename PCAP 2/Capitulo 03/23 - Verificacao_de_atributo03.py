# Verificação da existência de um atributo: continuação
#
# Não se esqueça que a função hasattr() também pode operar em classes. Pode utilizá-la para descobrir se uma variável de classe está disponível, tal como aqui no exemplo do editor.
#
# A função devolve True se a classe especificada contiver um determinado atributo, e False caso contrário.
#
# Consegue adivinhar o output do código? Execute-o para verificar as suas suposições.
#
# E mais um exemplo - veja o código abaixo e tente prever o seu output:
# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
#
# example_object = ExampleClass()
#
# print(hasattr(example_object, 'b'))
# print(hasattr(example_object, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))
#
#
# Foi bem sucedido? Execute o código para verificar as suas previsões.
#
# Muito bem, chegámos ao fim desta secção. Na secção seguinte vamos falar de métodos, uma vez que os métodos conduzem os objetos e os tornam ativos.

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

print()
print("Separacao")
print()

class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b'))
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b'))
print(hasattr(ExampleClass, 'a'))

