
Key takeaways

1. Uma stack é um objeto concebido para armazenar dados utilizando o modelo LIFO. A stack realiza geralmente pelo menos duas operações, denominadas push() e pop().

2. A implementação da stack num modelo processual levanta vários problemas que podem ser resolvidos pelas técnicas oferecidas pelo OOP (Object Oriented Programming):

3. Um método de classe é na realidade uma função declarada dentro da classe e capaz de aceder a todos os componentes da classe.

4. A parte da classe Python responsável pela criação de novos objetos é chamada de construtor, e é implementada como um método do nome __init__.

5. Cada declaração de método de classe deve conter pelo menos um parâmetro (sempre o primeiro) geralmente referido como self, e é usado pelos objetos para se identificarem.

6. Se quisermos esconder qualquer um dos componentes de uma classe do mundo exterior, devemos começar o seu nome com __. Tais componentes são chamados privados.


Exercício 1

Assumindo que existe uma classe chamada Snakes, escreva a primeira linha da declaração de classe Python , expressando o facto de a nova classe ser na realidade uma subclasse de Snake.

class Python(Snakes):



Exercício 2

Faltou alguma coisa na seguinte declaração — o quê?
class Snakes
    def __init__():
        self.sound = 'Sssssss'


A função __init__() não tem o parâmetro obrigatório (devemos nomeá-lo self para permanecer em conformidade com as normas).


Exercício 3

Modifique o código para garantir que a propriedade venomous é privada.
class Snakes
    def __init__(self):
        self.venomous = True
		

O código deve ter a seguinte aparência:

class Snakes
    def __init__(self):
        self.__venomous = True

