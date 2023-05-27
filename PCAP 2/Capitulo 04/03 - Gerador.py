# Geradores - onde encontrá-los: continuação
# 
# O exemplo anterior mostra uma solução em que o objeto iterador faz parte de uma classe mais complexa.
#
# O código não é realmente sofisticado, mas apresenta o conceito de forma clara.
#
# Dê uma vista de olhos ao código no editor.
#
# Nós construímos o iterador Fib noutra classe (podemos dizer que o compusemos na classe Class ). É instanciado juntamente com Classdo objeto.
#
# O objeto da classe pode ser usado como um iterador quando (e apenas quando) responde positivamente à invocação __iter__ - esta classe pode fazê-lo, e se for invocada desta forma, fornece um objeto capaz de # obedecer ao protocolo de iteração.
#
# É por isto que o output do código é o mesma que anteriormente, embora o objeto da classe Fib não seja usado explicitamente dentro do contexto do loop for .

class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;


object = Class(8)

for i in object:
    print(i)
