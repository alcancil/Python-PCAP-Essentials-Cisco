# Como construir uma hierarquia de classes: continuação
#
# Veja o código no editor novamente. Isto é o que fizemos:
#
#    definimos uma superclasse chamada Vehicle, que usa o método turn() para implementar um esquema geral de viragem, enquanto a viragem propriamente dita é feita por um método denominado change_direction(); # nota: o método anterior está vazio, pois vamos colocar todos os detalhes na subclasse (tal método é muitas vezes chamado método abstrato, pois demonstra apenas alguma possibilidade que será instanciada mais # tarde)
#     definimos uma subclasse chamada TrackedVehicle (nota: é derivada da classe Vehicle ) que instanciou o método change_direction() utilizando o método específico (concreto) denominado control_track()
#    respetivamente, a subclasse nomeada WheeledVehicle faz o mesmo truque, mas usa o método turn_front_wheels() para forçar o veículo a virar.
#
# A vantagem mais importante (omitindo questões de legibilidade) é que esta forma de código permite implementar um algoritmo de viragem novinho em folha, apenas modificando o método turn() , que pode ser 
# feito num só local, uma vez que todos os veículos o obedecerão.
# 
# É desta forma que o polimorfismo ajuda o programador a manter o código limpo e consistente.


import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        change_direction(left, True)
        time.sleep(0.25)
        change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        control_track(left, on)


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        turn_front_wheels(left, on)

