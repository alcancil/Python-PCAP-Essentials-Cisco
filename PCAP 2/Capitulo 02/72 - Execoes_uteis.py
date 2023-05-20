KeyboardInterrupt

Localização: BaseException ← KeyboardInterrupt

Descrição: uma exceção concreta levantada quando o utilizador utiliza um atalho de teclado concebido para terminar a execução de um programa (Ctrl-C na maioria dos sistemas operativos); se o tratamento desta exceção não levar à conclusão do programa, o programa continua a sua execução.

Nota: esta exceção não é derivada da Exception classe. Execute o programa em IDLE.

Código:
# This code cannot be terminated
# by pressing Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")


LookupError

Localização: BaseException ← Exception ← LookupError

Descrição: uma exceção abstrata incluindo todas as exceções causadas por erros resultantes de referências inválidas a diferentes coleções (listas, dicionários, tuples, etc.)


MemoryError

Localização: BaseException ← Exception ← MemoryError

Descrição: uma exceção concreta levantada quando uma operação não pode ser concluída devido a uma falta de memória livre.

Código:
# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')


OverflowError

Localização: BaseException ← Exception ← ArithmeticError ← OverflowError

Descrição: uma exceção concreta levantada quando uma operação produz um número demasiado grande para ser armazenado com sucesso

Código:
# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

