# Herança: isinstance()
#
# Como já sabe, um objeto é uma incarnação de uma classe. Isto significa que o objeto é como um bolo cozido utilizando uma receita que está incluída dentro da classe.
#
# Isto pode gerar alguns problemas importantes.
#
# Vamos supor que tem um bolo (por exemplo, como um argumento passado para a sua função). Você quer saber qual a receita utilizada para o fazer. Porquê? Porque quer saber o que esperar dele, por exemplo, se 
# contém nozes ou não, o que é uma informação crucial para algumas pessoas.
#
# Da mesma forma, pode ser crucial se o objeto tiver (ou não tiver) certas características. Por outras palavras, se é um objeto de uma determinada classe ou não.
#
# Tal facto pode ser detetado pela função chamada isinstance():
# isinstance(objectName, ClassName)
#
#
# As funções devolvem True se o objeto for uma instância da classe, ou False caso contrário.
#
# Ser uma instância de uma classe significa que o objeto (o bolo) foi preparado utilizando uma receita contida quer na classe quer numa das suas superclasses.
#
# Não se esqueça: se uma subclasse contém pelo menos o mesmo equipamento que qualquer uma das suas superclasses, significa que os objetos da subclasse podem fazer o mesmo que os objetos derivados da 
# superclasse, portanto, é uma instância da sua home class e de qualquer uma das suas superclasses.
#
# Vamos testá-lo. Analise o código no editor.
#
# Criámos três objetos, um para cada uma das classes. Em seguida, utilizando dois loops nested, verificamos todos os pares possíveis da classe de objeto para descobrir se os objetos são instâncias das 
# classes.
#
# Execute o código.
#
# Isto é o que obtemos:
# True	False	False	
# True	True	False	
# True	True	True	
#
# output
#
# Vamos novamente tornar o resultado mais legível:
# ↓ é uma instância de → 	Vehicle 	LandVehicle 	TrackedVehicle
# my_vehicle 	              True        False           	False
# my_land_vehicle 	        True 	  True 	            False
# my_tracked_vehicle 	        True 	  True 	            True
#
# Será que a tabela confirma as nossas expetativas?


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()
