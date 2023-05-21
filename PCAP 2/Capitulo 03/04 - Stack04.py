# A stack - a abordagem ao objeto: continuação
#
# Dê uma vista de olhos - adicionamos dois underscores antes do nome stack_list - nada mais:
class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()
print(len(stack_object.__stack_list))


# A alteração invalida o programa.
#
# Porquê?
#
# Quando qualquer componente de classe tem um nome que começa com dois underscores (__), torna-se privado - isto significa que só pode ser acedido de dentro da classe.
#
# Não se pode vê-lo do mundo exterior. É assim que o Python implementa o conceito de encapsulamento.
#
# Execute o programa para testar as nossas suposições - uma exceção AttributeError deve ser levantada.