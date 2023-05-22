# Variáveis de instância
#
# Em geral, uma classe pode ser equipada com dois tipos diferentes de dados para formar as propriedades de uma classe. Já viu um deles quando estávamos a olhar para stacks.
#
# Este tipo de propriedade de classe existe quando e só quando é explicitamente criada e adicionada a um objeto. Como já sabe, isto pode ser feito durante a inicialização do objeto, realizada pelo 
# construtor.
#
# Além disso, pode ser feito em qualquer momento da vida do objeto. Mais, qualquer propriedade existente pode ser removida em qualquer altura.
#
# Uma tal abordagem tem algumas consequências importantes:
#
#    objetos diferentes da mesma classe podem possuir conjuntos diferentes de propriedades;
#    deve haver uma forma de verificar com segurança se um objeto específico possui a propriedade que pretende utilizar (a menos que queira provocar uma exceção - vale sempre a pena considerar)
#    cada objeto carrega o seu próprio conjunto de propriedades - eles não interferem uns com os outros de forma alguma.
#
# Tais variáveis (propriedades) são chamadas variáveis de instância.
#
# A palavra instância sugere que elas estão intimamente ligadas aos objetos (que são instâncias de classe), não às classes propriamente ditas. Vamos dar-lhes uma olhadela mais atenta.
#
# Aqui está um exemplo:
class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val):
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)


# Precisa de uma explicação adicional antes de entrarmos em qualquer outro detalhe. Dê uma vista de olhos às três últimas linhas do código.
#
# Os objetos Python, quando criados, são dotados de um pequeno conjunto de propriedades e métodos pré-definidos. Cada objeto tem-nos, quer os queira ou não. Um deles é uma variável chamada __dict__ (é um 
# dicionário).
#
# A variável contém os nomes e valores de todas as propriedades (variáveis) que o objeto carrega atualmente. Vamos utilizá-la para apresentar o conteúdo de um objeto em segurança.
#
# Vamos agora mergulhar no código:
#
#    a classe nomeada ExampleClass tem um construtor, que cria incondicionalmente uma variável de instância chamada first, e define-a com o valor passado através do primeiro argumento (da perspetiva do 
# utilizador da classe) ou do segundo argumento (da perspetiva do construtor); note o valor por defeito do parâmetro - qualquer truque que se possa fazer com um parâmetro de função regular também pode ser 
# aplicado aos métodos;
#
#    a classe também tem um método que cria outra variável de instância, denominada second;
#
#    criámos três objetos da classe ExampleClass, mas todas estas instâncias diferem:
#
#        example_object_1 só tem a propriedade nomeada first;
#
#        example_object_2 tem duas propriedades: first e second;
#
#        example_object_3 foi enriquecido com uma propriedade chamada third enquanto em movimento, fora do código da classe - isto é possível e totalmente admissível.
#
# Os outputs do programa mostram claramente que os nossos pressupostos estão corretos - aqui está:
# {'first': 1}
# {'second': 3, 'first': 2}
# {'third': 5, 'first': 4}
#
# output
#
# Há uma conclusão adicional que deve ser afirmada aqui: a modificação de uma variável de instância de qualquer objeto não tem impacto em todos os objetos restantes. As variáveis de instância estão 
# perfeitamente isoladas umas das outras.