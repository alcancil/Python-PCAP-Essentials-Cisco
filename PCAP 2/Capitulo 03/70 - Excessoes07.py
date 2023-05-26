# Como criar a sua própria exceção: continuação
#
# Veja o código no editor. Juntámos as duas exceções previamente definidas e aproveitámo-las para trabalhar num pequeno trecho de exemplo.
#
# Um destes é levantado dentro do make_pizza() funcionam quando qualquer uma destas duas situações erradas é descoberta: um pedido de pizza errado, ou um pedido de demasiado queijo.
#
# Nota:
#
#    remoção do ramo a começar por except TooMuchCheeseError fará com que todas as exceções que aparecem sejam classificadas como PizzaError;
#    remoção do ramo a começar por except PizzaErrorwill causar as exceções TooMuchCheeseError a permanecer sem manuseio, e fará com que o programa termine.
#
#
# A solução anterior, embora elegante e eficiente, tem uma fraqueza importante. Devido à forma algo descontraída de declarar os construtores, as novas exceções não podem ser usadas tal como estão sem uma 
# lista completa dos argumentos requeridos.
#
# Vamos remover esta fraqueza ao definir os valores predefinidos para todos os parâmetros do construtor. Dê uma vista de olhos:

class PizzaError(Exception):
    def __init__(self, pizza='uknown', message=''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='uknown', cheese='>100', message=''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError
    if cheese > 100:
        raise TooMuchCheeseError
    print("Pizza ready!")


for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)


# Agora, se as circunstâncias o permitirem, é possível utilizar os nomes das classes sozinhos.

class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")

for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)
