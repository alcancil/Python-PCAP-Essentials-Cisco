# A abordagem de objeto: uma stack a partir do zero (continuação)
#
# Agora, vamos um pouco mais longe. Vamos adicionar uma nova classe para lidar com stacks.
#
# A nova classe deve ser capaz de avaliar a soma de todos os elementos atualmente armazenados na stack.
#
# Não queremos modificar a stack definida previamente. Já é suficientemente bom nas suas aplicações, e não queremos que seja alterado de forma alguma. Queremos uma nova stack com novas capacidades. Por 
# outras palavras, queremos construir uma subclasse da classe já existente Stack .
#
# O primeiro passo é fácil: basta definir uma nova subclasse apontando para a classe que será usada como a superclasse.
#
# Isto é o que parece:
# class AddingStack(Stack):
#    pass
#
#
# A classe ainda não define nenhum componente novo, mas isso não significa que esteja vazia. Recebe todos os componentes definidos pela sua superclasse - o nome da superclasse é escrito antes dos dois 
# pontos, diretamente após o nome da nova classe.
#
# Isto é o que queremos da nova stack:
#
#     queremos o método push não só para empurrar o valor para a stack, mas também para acrescentar o valor à variável sum ;
#     queremos a função pop não só para tirar o valor da stack, mas também para subtrair o valor da variável sum .
#
#
# Em primeiro lugar, vamos adicionar uma nova variável à classe. Será uma variável privada, como a lista de stack. Não queremos que ninguém manipule o valor sum .
#
# Como já sabe, adicionar uma nova propriedade à classe é feito pelo construtor. Já sabe como fazer isso, mas há algo realmente intrigante no interior do construtor. Dê uma vista de olhos:
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#
# A segunda linha do corpo do construtor cria uma propriedade chamada __sum - irá armazenar o total de todos os valores da stack.
#
# Mas a linha antes que pareça diferente. O que é que faz? É realmente necessário? Sim, é.
#
# Ao contrário de muitas outras linguagens, o Python obriga-o a invocar explicitamente o construtor de uma superclasse. Omitir este ponto terá efeitos nocivos - o objeto será privado da lista __stack_list . # Uma tal stack não funcionará corretamente.
#
# Esta é a única vez em que se pode invocar explicitamente qualquer um dos construtores disponíveis - pode ser feito dentro do construtor da subclasse.
#
# Observe a sintaxe:
#
#     especifica o nome da superclasse (esta é a classe cujo construtor pretende executar)
#     coloca um ponto (.) depois disso;
#     especifica o nome do construtor;
#     tem de apontar para o objeto (a instância da classe) que tem de ser inicializado pelo construtor - é por isso que tem de especificar o argumento e utilizar a variável self aqui; nota: a invocação de 
# qualquer método (incluindo construtores) de fora da classe nunca requer que se coloque o argumento self na lista do argumento - invocar um método de dentro da classe exige o uso explícito do argumento 
# self , e tem de ser colocado em primeiro lugar na lista.
#
# Nota: é geralmente uma prática recomendada invocar o construtor da superclasse antes de quaisquer outras inicializações que deseje realizar dentro da subclasse. Esta é a regra que temos seguido no  
# snippet.



class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0