# Como construir uma hierarquia de classes: continuação
# 
# A herança não é a única forma de construir classes adaptáveis. Pode-se alcançar os mesmos objetivos (nem sempre, mas muito frequentemente) usando uma técnica denominada composição.
#
# Composição é o processo de compor um objeto utilizando outros objetos diferentes. Os objetos utilizados na composição fornecem um conjunto de características desejadas (propriedades e/ou métodos) para que 
# possamos dizer que agem como blocos utilizados para construir uma estrutura mais complicada.
#
# Pode-se dizer que:
#
#    a herança alarga as capacidades de uma classe, acrescentando novos componentes e modificando os existentes; por outras palavras, a receita completa está contida dentro da própria classe e de todos os 
# seus antepassados; o objeto toma todos os pertences da classe e faz uso deles;
#    a composição projeta uma classe como um recipiente capaz de armazenar e utilizar outros objetos (derivados de outras classes) onde cada um dos objetos implementa uma parte do comportamento de uma classe # desejada.
#
# Vamos ilustrar a diferença utilizando os veículos previamente definidos. A abordagem anterior levou-nos a uma hierarquia de classes em que a classe mais alta estava ciente das regras gerais utilizadas na 
# viragem do veículo, mas não sabia como controlar os componentes apropriados (rodas ou lagartas).
#
# As subclasses implementaram esta capacidade através da introdução de mecanismos especializados. Vamos fazer (quase) a mesma coisa, mas usando a composição. A classe - como no exemplo anterior - está ciente # de como virar o veículo, mas a viragem real é feita por um objeto especializado armazenado numa propriedade chamada controller. A classe controller é capaz de controlar o veículo, manipulando as peças 
# relevantes do veículo.
#
# Dê uma vista de olhos ao editor - é assim que poderia parecer.
#
# Existem duas classes nomeadas Tracks e Wheels - elas sabem controlar a direção do veículo. Há também uma classe chamada Vehicle que pode utilizar qualquer um dos controladores disponíveis (os dois já 
# definidos, ou qualquer outro definido no futuro) - a controller é ela própria passada para a classe durante a iniciação.
#
# Desta forma, a capacidade de viragem do veículo é composta utilizando um objeto externo, não implementado no interior da Vehicle classe.
#
# Por outras palavras, temos um veículo universal e podemos instalar nele tanto lagartas como rodas.
#
# O código produz o seguinte output:
# wheels:  True True
# wheels:  True False
# tracks:  False True
# tracks:  False False


import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

