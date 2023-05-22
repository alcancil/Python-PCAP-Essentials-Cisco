# A abordagem de objeto: uma stack a partir do zero (continuação)
#
# Em segundo lugar, vamos acrescentar dois métodos. Mas deixe-nos perguntar-lhe: está realmente a acrescentar? Já temos estes métodos na superclasse. Podemos fazer algo assim?
#
# Sim, podemos. Isto significa que vamos alterar a funcionalidade dos métodos, não os seus nomes. Podemos dizer mais precisamente que a interface (a forma como os objetos são manuseados) da classe permanece a # mesma quando se altera a implementação ao mesmo tempo.
#
# Vamos começar com a implementação da função push . Isto é o que esperamos dela:
#
#    acrescentar o valor à variável __sum ;
#    empurrar o valor para a stack.
#
# Nota: a segunda atividade já foi implementada dentro da superclasse - por isso podemos utilizá-la. Além disso, temos de o utilizar, uma vez que não há outra forma de aceder à variável __stackList .
#
# É assim que o método push se parece na subclasse:
# def push(self, val):
#     self.__sum += val
#     Stack.push(self, val)
#
#
# Note-se a forma como invocámos a implementação anterior do método push (o disponível na superclasse):
#
#    temos de especificar o nome da superclasse; isto é necessário para indicar claramente a classe que contém o método, para evitar confundi-la com qualquer outra função do mesmo nome;
#    temos de especificar o objeto alvo e de o passar como primeiro argumento (não é implicitamente acrescentado à invocação neste contexto).
#
# Dizemos que o método push foi substituído - o mesmo nome que na superclasse representa agora uma funcionalidade diferente.

class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


# Enter code here.