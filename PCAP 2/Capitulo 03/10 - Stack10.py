# A abordagem de objeto: uma stack a partir do zero (continuação)
#
# Este é a nova função pop :
# def pop(self):
#     val = Stack.pop(self)
#     self.__sum -= val
#     return val
#
# 
# Até agora, definimos a variável __sum , mas não fornecemos um método para obter o seu valor. Parece estar escondido. Como podemos revelá-lo e fazê-lo de uma forma que ainda o proteja de modificações?
#
# Temos de definir um novo método. Vamos nomeá-lo get_sum. A sua única tarefa será devolver o valor __sum .
#
# Aqui está:
# def get_sum(self):
#     return self.__sum
#
#
# Portanto, vejamos o programa no editor. O código completo da classe está lá. Podemos verificar o seu funcionamento agora, e fazemo-lo com a ajuda de muito poucas linhas adicionais de código.
#
# Como pode ver, adicionamos cinco valores subsequentes à stack, imprimimos a sua soma, e retiramo-los todos da stack.
#
# Muito bem, esta foi uma introdução muito breve à programação de objetos de Python. Em breve vamos falar-lhe de tudo isto com mais detalhe.

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())