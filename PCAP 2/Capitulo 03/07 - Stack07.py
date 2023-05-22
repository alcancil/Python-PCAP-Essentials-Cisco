# A abordagem de objeto: uma stack a partir do zero (continuação)
#
# Analise o snippet abaixo - criámos três objetos da classe Stack. A seguir, fizemos malabarismos com eles. Tente prever o valor de output no ecrã.
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


little_stack = Stack()
another_stack = Stack()
funny_stack = Stack()

little_stack.push(1)
another_stack.push(little_stack.pop() + 1)
funny_stack.push(another_stack.pop() - 2)

print(funny_stack.pop())


# Então, qual é o resultado? Execute o programa e verifique se estava certo.