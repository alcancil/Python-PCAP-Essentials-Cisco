# Geradores - onde encontrá-los: continuação
#
# O protocolo iterador é uma forma de um objeto se comportar de acordo com as regras impostas pelo contexto das declarações for e in . Um objeto em conformidade com o protocolo iterador é chamado um iterador.
#
# Um iterador deve fornecer dois métodos:
#
#    __iter__() que deve devolver o objeto em si e que é invocado uma vez (é necessário para que Python inicie com sucesso a iteração)
#    __next__() que se destina a devolver o próximo valor (primeiro, segundo, etc.) da série desejada - será invocado pelas declarações for/in a fim de passar pela próxima iteração; se não houver mais valores # a fornecer, o método deve levantar a exceção StopIteration .
#
# Parece estranho? De modo algum. Veja o exemplo no editor.
#
# Construímos uma classe capaz de iterar através dos primeiros valores n (onde n é um parâmetro construtor) dos números de Fibonacci.
#
# Recordemos - os números Fibonacci (Fibi) são definidos da seguinte forma:
#
# Fib1 = 1
# Fib2 = 1
# Fibi = Fibi-1 + Fibi-2
# 
# Por outras palavras:
# 
#     os dois primeiros números de Fibonacci são iguais a 1;
#     qualquer outro número de Fibonacci é a soma dos dois anteriores (por exemplo, Fib3 = 2, Fib4 = 3, Fib5 = 5, e assim por diante)
# 
# Vamos mergulhar no código:
#
#    linhas 2 a 6: o construtor da classe imprime uma mensagem (vamos usá-la para rastrear o comportamento da classe), prepara algumas variáveis (__n para armazenar o limite da série, __i para rastrear o 
# número atual de Fibonacci a fornecer, e __p1 juntamente com __p2 para guardar os dois números anteriores);
#
#    linhas 8 a 10: o método __iter__ é obrigado a devolver o próprio objeto iterador; o seu objetivo pode ser um pouco ambíguo aqui, mas não há mistério; tente imaginar um objeto que não seja um iterador 
# (por exemplo, é uma coleção de algumas entidades), mas um dos seus componentes é um iterador capaz de digitalizar a coleção; o método __iter__ deve extrair o iterador e confiar-lhe a execução do protocolo 
# de iteração; como pode ver, o método inicia a sua ação imprimindo uma mensagem;
#
#    linhas 12 a 21: o método __next__ é responsável pela criação da sequência; é um tanto ou quanto minucioso, mas isto deve torná-lo mais legível; primeiro, imprime uma mensagem, depois atualiza o número de # valores desejados, e se chegar ao fim da sequência, o método quebra a iteração levantando a exceção StopIteration; o resto do código é simples, e reflete precisamente a definição que lhe mostrámos 
# anteriormente;
#
#    as linhas 24 e 25 fazem uso do iterador.


class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)