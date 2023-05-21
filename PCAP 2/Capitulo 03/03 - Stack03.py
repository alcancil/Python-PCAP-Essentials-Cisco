# A stack - a abordagem ao objeto: continuação
#
# Qualquer mudança que faça no interior do construtor que modifique o estado do parâmetro self será refletido no objeto recém-criado.
#
# Isto significa que se pode acrescentar qualquer propriedade ao objeto e a propriedade permanecerá lá até que o objeto termine a sua vida ou a propriedade seja explicitamente removida.
#
# Agora vamos adicionar apenas uma propriedade ao novo objeto - uma lista para uma stack. Vamos nomeá-lo stack_list.
#
# Tal como aqui:
# class Stack:
#    def __init__(self):
#        self.stack_list = []
#
#
# stack_object = Stack()
# print(len(stack_object.stack_list))
#
#
# Nota:
#
#    utilizámos a notação pontilhada, tal como quando invocamos métodos; esta é a convenção geral para aceder às propriedades de um objeto - é necessário dar um nome ao objeto, colocar um ponto (.) depois 
# dele, e especificar o nome da propriedade desejada; não use parêntesis! Não deseja invocar um método - deseja aceder a uma propriedade;
#    se definir o valor de uma propriedade pela primeira vez (como no construtor), está a criá-la; a partir desse momento, o objeto tem a propriedade e está pronto a usar o seu valor;
#    fizemos algo mais no código - tentámos aceder à propriedade stack_list de fora da classe imediatamente após o objeto ter sido criado; queremos verificar o comprimento atual da stack - conseguimos?
#
# Sim, conseguimos - o código produz o seguinte output:
# 0
#
# output
#
# Isto não é que queremos da stack. Preferimos que stack_list seja ocultado do mundo exterior. Será isso possível?
#
# Sim, e é simples, mas não muito intuitivo.

class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))