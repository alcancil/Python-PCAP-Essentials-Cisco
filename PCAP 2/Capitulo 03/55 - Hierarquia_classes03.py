# Como construir uma hierarquia de classes: continuação
#
# Veja o exemplo no editor.
#
# Parece-se com alguma coisa? Sim, claro que sim. Refere-se ao exemplo mostrado no início do módulo quando falamos sobre os conceitos gerais da programação objetiva.
#
# Pode parecer estranho, mas não utilizámos a herança de forma alguma - apenas para mostrar que ela não nos limita, e conseguimos obter a nossa.
#
# Definimos duas classes distintas capazes de produzir dois tipos diferentes de veículos terrestres. A principal diferença entre eles está na forma como viram. Um veículo com rodas apenas vira as rodas da 
# frente (geralmente). Um veículo com lagartas tem de parar uma das lagartas.
#
# Consegue seguir o código?
#
#    um veículo com lagartas faz uma curva ao parar e deslocar-se numa das suas lagartas (isto é feito pelo método control_track() , que será implementado mais tarde)
#    um veículo com rodas gira quando as suas rodas da frente giram (isto é feito pelo método turn_front_wheels() )
#    o método turn() utiliza o método adequado para cada veículo em particular.
#
# Consegue ver o que está errado com o código?
#
# Os métodos turn() parecem demasiado semelhantes para os deixar nesta forma.
#
# Vamos reconstruir o código - vamos introduzir uma superclasse para reunir todos os aspetos semelhantes dos veículos de condução, deslocando todos os aspetos específicos para as subclasses.

import time

class TrackedVehicle:
    def control_track(left, stop):
        pass

    def turn(left):
        control_track(left, True)
        time.sleep(0.25)
        control_track(left, False)


class WheeledVehicle:
    def turn_front_wheels(left, on):
        pass

    def turn(left):
        turn_front_wheels(left, True)
        time.sleep(0.25)
        turn_front_wheels(left, False)
