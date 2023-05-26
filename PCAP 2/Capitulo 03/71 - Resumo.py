
Key takeaways

1. A função else: da declaração try é executado quando não houve nenhuma exceção durante a execução do bloco try: .

2. O método finally: da declaração try é sempre executado.

3. A sintaxe except Exception_Name as an exception_object: permite-lhe interceptar um objeto portador de informação sobre uma exceção pendente. A propriedade do objeto chamada args (um tuple) armazena todos os argumentos passados para o construtor do objeto.

4. As classes de exceção podem ser alargadas para as enriquecer com novas capacidades, ou para adotar as suas características a novas exceções definidas.

Por exemplo:
try:
    assert __name__ == "__main__"
except:
    print("fail", end=' ')
else:
    print("success", end=' ')
finally:
    print("done")


O código faz o output: success done.

Exercício 1

Qual é o output esperado do seguinte código?
import math

try:
    print(math.sqrt(9))
except ValueError:
    print("inf")
else:
    print("fine")


3.0
fine


Exercício 2

Qual é o output esperado do seguinte código?
import math

try:
    print(math.sqrt(-9))
except ValueError:
    print("inf")
else:
    print("fine")
finally:
    print("the end")


inf
the end


Exercício 3

Qual é o output esperado do seguinte código?
import math

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")
except NewValueError as nve:
    for arg in nve.args:
        print(arg, end='! ')


Enemy warning! Red alert! High readiness! 
