# A abordagem ao objeto: uma stack do zero
# 
# A gora é altura de as duas funções (métodos) implementarem as operações push e pop. O Python assume que uma função deste tipo (uma atividade de classe) deve ser imersa dentro do corpo da classe - tal como # um construtor.
#
# Queremos invocar estas funções para valores push e pop . Isto significa que ambos devem ser acessíveis a todos os utilizadores da classe (em contraste com a lista previamente construída, que está 
# escondida dos utilizadores comuns da classe).
#
# Tal componente é chamado público, pelo que não se pode começar o seu nome com dois (ou mais) underscores. Há mais um requisito - o nome não deve ter mais do que um underscore à direita. Uma vez que nenhum # underscore à direita satisfaz totalmente o requisito, pode-se assumir que o nome é aceitável.
#
# As funções em si são simples. Dê uma vista de olhos:
# class Stack:
#    def __init__(self):
#        self.__stack_list = []
#
#    def push(self, val):
#        self.__stack_list.append(val)
#
#    def pop(self):
#        val = self.__stack_list[-1]
#        del self.__stack_list[-1]
#        return val
#
#
# stack_object = Stack()
#
# stack_object.push(3)
# stack_object.push(2)
# stack_object.push(1)
#
# print(stack_object.pop())
# print(stack_object.pop())
# print(stack_object.pop())
#
#
# No entanto, há algo realmente estranho no código. As funções parecem familiares, mas têm mais parâmetros do que as suas contrapartes processuais.
#
# Aqui, ambas as funções têm um parâmetro chamado self na primeira posição da lista de parâmetros.
#
# É necessário? Sim, é.
#
# Todos os métodos têm de ter este parâmetro. Desempenha o mesmo papel que o primeiro parâmetro construtor.
#
# Permite ao método aceder a entidades (propriedades e atividades/métodos) realizadas pelo objeto atual. Não se pode omiti-lo. Sempre que o Python invoca um método, envia implicitamente o objeto atual como # o primeiro argumento.
#
# Isto significa que um método é obrigado a ter pelo menos um parâmetro, que é utilizado pelo próprio Python - não tem qualquer influência sobre ele.
#
# Se o seu método não necessita de parâmetros, este deve ser especificado de qualquer forma. Se for concebido para processar apenas um parâmetro, é necessário especificar dois, e o primeiro continua a ter o # mesmo papel.
#
# Há mais uma coisa que requer explicação - a forma como os métodos são invocados a partir do interior da variável __stack_list .
#
# Felizmente, é muito mais simples do que parece:
#
#    a primeira fase entrega o objeto como um todo → self;
#    a seguir, precisa de chegar à __stack_list lista → self.__stack_list;
#    com __stack_list pronto a ser utilizado, pode executar o terceiro e último passo → self.__stack_list.append(val).
#
# A declaração de classe está completa, e todos os seus componentes foram listados. A classe está pronta a ser utilizada.


class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())