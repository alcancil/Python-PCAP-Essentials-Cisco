# Exercícios
#
# Cenário
#
# Suponha que o seguinte snippet de código foi executado com sucesso:

class Dog:
    kennel = 0
    def __init__(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def __str__(self):
        return self.breed + " says: Woof!"


class SheepDog(Dog):
    def __str__(self):
        return super().__str__() + " Don't run away, Little Lamb!"


class GuardDog(Dog):
    def __str__(self):
        return super().__str__() + " Stay where you are, Mister Intruder!"


rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")


# Agora responda às perguntas dos exercícios 1-4.
#
#
# Exercício 1
#
# Qual é o output esperado do seguinte snippet de código?
#
# print(rocky)
# print(luna)
#
# Collie says: Woof! Don't run away, Little Lamb!
# Dobermann says: Woof! Stay where you are, Mister Intruder!
#
#
# Exercício 2
#  
# Qual é o output esperado do seguinte snippet de código?
#
print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))

# True False
# False True
#
#
# Exercício 3
#
# Qual é o output esperado do seguinte snippet de código?

print(luna is luna, rocky is luna)
print(rocky.kennel)


# 
# Exercício 4
#
# Defina uma subclasse SheepDogchamada LowlandDog, e equipe-a com um método __str__() que substitui um método herdado com o mesmo nome. O novo método dog's __str__() deve devolver a string “Woof! I don't 
# like mountains!" .

class LowlandDog(SheepDog):
	def __str__(self):
		return Dog.__str__(self) + " I don't like mountains!"
		
