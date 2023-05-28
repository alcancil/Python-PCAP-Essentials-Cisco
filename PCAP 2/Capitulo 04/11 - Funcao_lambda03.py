# Lambdas e a função map() .
#
# No mais simples de todos os casos possíveis, a função map() .
#
# map(function, list)
#
# toma dois argumentos:
#
#    uma função;
#    uma lista.
#
# A descrição acima é extremamente simplificada, uma vez que:
#
#    o segundo argumento map() pode ser qualquer entidade que possa ser iterada (por exemplo, um tuple, ou apenas um gerador)
#    map() pode aceitar mais de dois argumentos.
#
# A função map() aplica a função passada pelo seu primeiro argumento a todos os elementos do seu segundo argumento, e devolve um iterador entregando todos os resultados subsequentes da função.
#
# Pode usar o iterador resultante num loop, ou convertê-lo numa lista usando a função list() .
#
# Consegue ver aqui um papel para qualquer lambda?
#
# Veja o código no editor - utilizámos dois lambdas no mesmo.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# Esta é a intriga:
#
#    construa o list_1 com valores de 0 até 4;
#    em seguida, utilize map juntamente com o primeiro lambda para criar uma nova lista na qual todos os elementos tenham sido avaliados como 2 elevados à potência retirada do elemento correspondente de 
# list_ 1; 
#    list_2 é então impresso;
#    no passo seguinte, utilize a função map() novamente para fazer uso do gerador que devolve e para imprimir diretamente todos os valores que fornece; como pode ver, envolvemos o segundo lambda aqui - 
# apenas eleva ao quadrado cada elemento de list_2.
#
# Tente imaginar o mesmo código sem lambdas. Seria melhor? É pouco provável.