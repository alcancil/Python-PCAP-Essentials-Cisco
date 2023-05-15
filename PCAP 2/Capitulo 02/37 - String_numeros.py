# Strings vs. números
#
# Há duas questões adicionais que devem ser discutidas aqui: como converter um número (um número inteiro ou um float) numa string, e vice-versa. Pode ser necessário realizar tal transformação. Além disso, é 
# uma forma rotineira de processar dados de input/output.
#
# A conversão número-string é simples, pois é sempre possível. É feita por uma função chamada str().
#
# Tal como aqui:
# itg = 13
# flt = 1.3
# si = str(itg)
# sf = str(flt)
#
# print(si + ' ' + sf)
#
#
# Output do código:
# 13 1.3
# 
# output
#
# A transformação inversa (string-número) é possível quando e só quando a string representa um número válido. Se a condição não for cumprida, espere uma ValueError .
#
# Utilize a função int() , se quiser obter um número inteiro, e float() se precisar de um valor de floating-point.
#
# Tal como aqui:
# si = '13'
# sf = '1.3'
# itg = int(si)
# flt = float(sf)
# 
# print(itg + flt)
#
#
# Isto é o que verá na consola:
# 14.3
#
# output
#
# Na secção seguinte, vamos mostrar-lhe alguns programas simples que processam strings.
