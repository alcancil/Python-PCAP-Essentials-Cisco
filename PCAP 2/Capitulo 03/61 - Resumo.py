# Key takeaways
# 
# 1. Um método chamado __str__() é responsável pela conversão do conteúdo de um objeto numa string (mais ou menos) legível. Pode redefini-la se quiser que o seu objeto se possa apresentar de uma forma mais  #elegante. Por exemplo:

class Mouse:
    def __init__(self, name):
        self.my_name = name


    def __str__(self):
        return self.my_name


the_mouse = Mouse('mickey')
print(the_mouse)  # Prints "mickey". 


# 2. Uma função chamada issubclass(Class_1, Class_2) é capaz de determinar se Class_1 é uma subclasse de Class_2. Por exemplo:
class Mouse:
    pass


class LabMouse(Mouse):
    pass


print(issubclass(Mouse, LabMouse), issubclass(LabMouse, Mouse))  # Prints "False True"


# 3. Uma função chamada isinstance(Object, Class) verifica se um objeto vem de uma classe indicada. Por exemplo:
class Mouse:
    pass


class LabMouse(Mouse):
    pass


mickey = Mouse()
print(isinstance(mickey, Mouse), isinstance(mickey, LabMouse))  # Prints "True False".


# 4. Um operador chamado is verifica se duas variáveis se referem ao mesmo objeto. Por exemplo:
class Mouse:
    pass


mickey = Mouse()
minnie = Mouse()
cloned_mickey = mickey
print(mickey is minnie, mickey is cloned_mickey)  # Prints "False True".



# 5. Uma função sem parâmetros chamada super() devolve uma referência para a superclasse mais próxima da classe. Por exemplo:
class Mouse:
    def __str__(self):
        return "Mouse"


class LabMouse(Mouse):
    def __str__(self):
        return "Laboratory " + super().__str__()


doctor_mouse = LabMouse();
print(doctor_mouse)  # Prints "Laboratory Mouse".


# 6. Os métodos, bem como as variáveis de instância e classe definidas numa superclasse, são automaticamente herdados pelas suas subclasses. Por exemplo:
class Mouse:
    Population = 0
    def __init__(self, name):
        Mouse.Population += 1
        self.name = name

    def __str__(self):
        return "Hi, my name is " + self.name

class LabMouse(Mouse):
    pass

professor_mouse = LabMouse("Professor Mouser")
print(professor_mouse, Mouse.Population)  # Prints "Hi, my name is Professor Mouser 1"


# 7. Para encontrar qualquer propriedade objeto/classe, o Python procura-a no interior:
#
#    do objeto em si;
#    de todas as classes envolvidas na linha de herança do objeto, de baixo para cima;
#    se houver mais do que uma classe num determinado caminho de herança, o Python digitaliza-as da esquerda para a direita;
#    se ambos acima falharem, a exceção AttributeError é levantada.
#
#
# 8. Se qualquer uma das subclasses definir uma variável de método/classe variável/instância com o mesmo nome que a existente na superclasse, o novo nome sobrepõe-se a qualquer uma das instâncias anteriores # do nome. Por exemplo:
class Mouse:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name

class AncientMouse(Mouse):
    def __str__(self):
        return "Meum nomen est " + self.name

mus = AncientMouse("Caesar")  # Prints "Meum nomen est Caesar"
print(mus)

