# De que forma o Python encontra propriedades e métodos
# 
# Vamos agora ver como o Python lida com métodos de herança.
#
# Dê uma vista de olhos no exemplo no editor. Vamos analisá-lo:
#
#    há uma classe chamada Super, que define o seu próprio construtor, usado para atribuir a propriedade do objeto, chamada name.
#    a classe também define o método __str__() , o que torna a classe capaz de apresentar a sua identidade na forma de um texto claro.
#    a classe é então utilizada como base para criar uma subclasse chamada Sub. A classe Sub define o seu próprio construtor, que invoca o da superclasse. Observe como o fizemos: Super.__init__(self, name).
#    nomeámos explicitamente a superclasse, e apontámos para o método para invocar __init__(), fornecendo todos os argumentos necessários.
#    instanciámos um objeto de classe Sub e imprimimo-lo.
#
# Output do código:
# My name is Andy.
#
# output
#
# Nota: Como não há um método __str__() dentro da classe Sub , a string impressa deve ser produzida dentro da classe Super . Isto significa que o método __str__() foi herdado pela classe Sub .

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")

print(obj)
