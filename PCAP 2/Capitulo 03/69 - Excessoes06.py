# Como criar a sua própria exceção: continuação
#
# Quando se vai construir um universo completamente novo cheio de criaturas completamente novas que não têm nada em comum com todas as coisas familiares, pode querer construir a sua própria estrutura de 
# exceção.
#
# Por exemplo, se trabalhar num grande sistema de simulação destinado a modelar as atividades de um restaurante de pizza, pode ser desejável formar uma hierarquia separada de exceções.
#
# Pode começar a construí-la definindo uma exceção geral como uma nova classe base para qualquer outra exceção especializada. Fizemo-lo da seguinte forma:

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


# Nota: vamos recolher aqui informações mais específicas do que uma regular Exception faz, pelo que o nosso construtor aceitará dois argumentos:
#
#    um que especifique uma pizza como um assunto do processo,
#    e um que contenha uma descrição mais ou menos precisa do problema.
#
# Como pode ver, passamos o segundo parâmetro ao construtor de superclasse, e guardamos o primeiro dentro da nossa própria propriedade.
#
# Um problema mais específico (como um excesso de queijo) pode exigir uma exceção mais específica. É possível derivar a nova classe a partir da classe já definida PizzaError , como fizemos aqui:

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError._init__(self, pizza, message)
        self.cheese = cheese


# A exceção TooMuchCheeseError precisa de mais informações do que a exceção regular PizzaError , por isso adicionamo-la ao construtor - o nome cheese é então armazenado para processamento posterior.