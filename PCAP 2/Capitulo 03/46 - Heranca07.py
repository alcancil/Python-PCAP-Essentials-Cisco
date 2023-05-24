# Como o Python encontra propriedades e métodos: continuação
#
# Veja o código no editor. Modificámo-lo para lhe mostrar outro método de acesso a qualquer entidade definida dentro da superclasse.
#
# No último exemplo, nomeámos explicitamente a superclasse. Neste exemplo, fazemos uso da função super() , que acede à superclasse sem a necessidade de saber o seu nome:
# super().__init__(name)
#
#
# A função super() cria um contexto em que não é necessário (além disso, não se deve) passar o argumento self ao método invocado - é por isso que é possível ativar o construtor da superclasse usando apenas um # argumento.
#
# Nota: pode utilizar este mecanismo não só para invocar o construtor da superclasse, mas também para ter acesso a qualquer um dos recursos disponíveis dentro da superclasse.
#
#
#    Sandbox
#
# Code
#

class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Andy")

print(obj)

