# Os loops ctime() .
#
# A função time fornece uma função chamada ctime, que converte o tempo em segundos desde 1 de janeiro de 1970 (época Unix) para uma string.
#
# Lembra-se do resultado da função time ? É isso que precisa de passar para ctime. Dê uma vista de olhos no exemplo no editor.

import time

timestamp = 1572879180
print(time.ctime(timestamp))
print()

# Resultado:
# Mon Nov  4 14:53:00 2019
#
# output
#
# A função ctime devolve uma string para o timestamp passado. No nosso exemplo, o timestamp expressa 4 de novembro de 2019 às 14:53:00.
#
# Também é possível chamar a função ctime sem especificar o tempo em segundos. Neste caso, a hora atual será devolvida:
#

import time
print(time.ctime())

