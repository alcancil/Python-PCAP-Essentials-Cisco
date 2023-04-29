# Tuplas
# ----------
#
# Tuplas são um tipo de coleção onde os ítens armezanos vão estar ( ) . Mas não existem Tuplas vazias e nem com um único íten dentro dela. Se colocarmo um ítem, por exemplo ( 1 ) ou ( "carro" )
# será uma váriavel e não um ítem de uma tupla. Porém para informar uma tupla com um único ítem devemos fazer assim: ( 1, ). Nesse exemplo colocamos um elemento 1 e depois a virgula indicando que
# o segundo ítem é vazio. Cabe aqui também ressaltar que as Tuplas são muito parecidas com listas porém elas são IMUTÁVEIS, ou seja, não é possível realizar a adição ou subtraçõ de ítens da TUPLA.
# As tuplas possuem somente os ítens dentro dela sem qualquer tipo de indice.
#
# Como usar um tuple?
#
# Se quiser obter os elementos de um tuple a fim de os ler, pode utilizar as mesmas convenções a que está habituado enquanto utiliza listas.
#
# Dê uma vista de olhos ao código no editor.
#
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# O programa deve produzir o seguinte output - execute-o e verifique:
# 1
# 1000
# (10, 100, 1000)
# (1, 10)
# 1
# 10
# 100
# 1000
# 
# output
# 
# As semelhanças podem ser enganadoras - não tente modificar o conteúdo de um tuple! Não é uma lista!
# 
# Todas estas instruções (exceto a mais acima) causarão um erro de runtime:
# my_tuple = (1, 10, 100, 1000)
# 
# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10
# 
# 
# Esta é a mensagem que o Python lhe dará na janela da consola:
# AttributeError: 'tuple' object has no attribute 'append'