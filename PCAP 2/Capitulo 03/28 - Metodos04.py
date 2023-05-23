# Métodos em detalhe: continuação
#
# Como __init__ é um método, e um método é uma função, pode-se fazer os mesmos truques com construtores/métodos que se fazem com funções comuns.
#
# O exemplo no editor mostra como definir um construtor com um valor de argumento padrão. Teste-o.
#
# Output do código:
# object
# None
#
# output
#
# Tudo o que dissemos sobre mangling de nome de propriedade aplica-se também a nomes de métodos - um método cujo nome começa com __ está (parcialmente) oculto.
#
# O exemplo mostra este efeito:
class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()
except:
    print("failed")

obj._Classy__hidden()


# Output do código:
# visible
# failed
# hidden
#
# output
#
# Execute o programa e teste-o.