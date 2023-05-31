

# Os loops strftime() no módulo time .
#
# Provavelmente não ficará surpreendido por saber que a função strftime está disponível no módulo time . Difere ligeiramente dos métodos strftime nas classes fornecidas pelo módulo datetime porque, para além # do argumento format, também pode levar (opcionalmente) um tuple ou um objeto struct_time.
#
# Se não passar um tuple ou um objeto struct_time, a formatação será feita utilizando a hora local atual. Dê uma vista de olhos no exemplo no editor.
#
# O nosso resultado é o seguinte:
# 2019/11/04 14:53:00
# 2020/10/12 12:19:40
#
# output de amostra
#
# A criação de um format tem o mesmo aspeto que para os métodos strftime no módulo datetime . No nosso exemplo, usamos as diretivas %Y, %m, %d, %H, %M, e %S que já conhece.
#
# Na primeira chamada de função, formatamos o objeto struct_time, enquanto na segunda chamada (sem o argumento opcional), formatamos a hora local. Pode encontrar todas as diretivas disponíveis no módulo time # aqui.

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))
