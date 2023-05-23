# Verificação da existência de um atributo
#
# A atitude do Python em relação à instanciação de objetos levanta uma questão importante - em contraste com outras linguagens de programação, não se pode esperar que todos os objetos da mesma classe tenham o # mesmo conjunto de propriedades.
#
# Assim como no exemplo no editor. Olhe com atenção.
#
# O objeto criado pelo construtor pode ter apenas um dos dois atributos possíveis: a ou b.
#
# A execução do código produzirá o seguinte output:
# 1
# Traceback (most recent call last):
#   File ".main.py", line 11, in 
#     print(example_object.b)
# AttributeError: 'ExampleClass' object has no attribute 'b'
#
# output
#
# Como pode ver, o acesso a um atributo de objeto (classe) inexistente causa uma AttributeError exceção.
#
#
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)