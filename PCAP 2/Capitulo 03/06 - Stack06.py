# A abordagem ao objeto: uma stack do zero
#
# Ter uma tal classe abre algumas novas possibilidades. Por exemplo, pode agora ter mais do que uma stack a comportar-se da mesma maneira. Cada stack terá a sua própria cópia de dados privados, mas utilizará # o mesmo conjunto de métodos.
#
# Isto é exatamente o que queremos para este exemplo.
#
# Analise o código:
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())

print(stack_object_2.pop())


# Existem duas stacks criadas a partir da mesma classe base. Elas trabalham de forma independente. Pode fazer mais delas se o desejar.
#
# Execute o código no editor e veja o que acontece. Realize as suas próprias experiências.
