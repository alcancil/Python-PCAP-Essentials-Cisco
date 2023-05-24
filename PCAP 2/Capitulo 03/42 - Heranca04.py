# Herança: issubclass()
#
# O Python oferece uma função que é capaz de identificar uma relação entre duas classes, e embora o seu diagnóstico não seja complexo, pode verificar se uma determinada classe é uma subclasse de qualquer 
# outra classe.
#
# É este o seu aspeto:
# issubclass(ClassOne, ClassTwo)
#
#
# A função devolve True Se ClassOne for uma subclasse de ClassTwo, e False caso contrário.
#
# Vamos vê-lo em ação - pode surpreendê-lo. Veja o código no editor. Leia-o com atenção.
#
# Existem dois loops nested. O seu objetivo é verificar todos os pares de classes ordenados possíveis, e imprimir os resultados da verificação para determinar se o par corresponde à relação subclasse-
# superclasse.
#
# Execute o código. O programa produz o seguinte output:
# True	False	False	
# True	True	False	
# True	True	True	
#
# output
#
# Vamos tornar o resultado mais legível:
# ↓ é uma subclasse de → 	Vehicle 	LandVehicle 	TrackedVehicle
# Vehicle 	                   True 	    False             False
# LandVehicle 	             True 	     True 	          False
# TrackedVehicle 	             True 	     True 	          True
# 
# Há uma observação importante a fazer: cada classe é considerada como uma subclasse de si mesma.

class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()
