# A vida interior das classes e objetos
#
# Cada classe de Python e cada objeto de Python é pré-equipada com um conjunto de atributos úteis que podem ser utilizados para examinar as suas capacidades.
#
# Já conhece um destes - é a propriedade __dict__ .
#
# Vamos observar como lida com os métodos - vejamos o código no editor.
#
# Execute-o para ver o seu output. Verifique o output com cuidado.
#
# Encontre todos os métodos e atributos definidos. Localize o contexto no qual eles existem: dentro do objeto ou dentro da classe.
#

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print(obj.__dict__)
print(Classy.__dict__)