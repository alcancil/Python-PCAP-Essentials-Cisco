# Os loops find() .
#
# A classe find() é semelhante a index(), que já conhece - procura uma substring e devolve o index de primeira ocorrência desta substring, mas:
#
#     é mais seguro - não gera um erro para um argumento que contém uma substring inexistente (devolve -1 então)
#     funciona apenas com strings - não tente aplicá-lo a qualquer outra sequência.
#
# Veja o código no editor. É assim que pode utilizá-lo.
#
# O exemplo imprime:
# 1
# -1
#
# output
# 
# Nota: não use find() se quiser apenas verificar se um único caratere ocorre dentro de uma string - o operador in será significativamente mais rápido.
# 
# Aqui está outro exemplo:
# t = 'theta'
# print(t.find('eta'))
# print(t.find('et'))
# print(t.find('the'))
# print(t.find('ha'))
#
# 
# Consegue prever o output? Execute-o e verifique as suas previsões.
#
# Se quiser realizar a procura, não desde o início da string, mas a partir de qualquer posição, pode usar uma variante de dois parâmetros do find() método. Veja o exemplo:
# print('kappa'.find('a', 2))
#
#
# O segundo argumento especifica o index em que a pesquisa será iniciada (não tem de caber dentro da string).
#
# Entre as duas letras a, apenas a segunda será encontrada. Execute o snippet e verifique.
#
# Pode utilizar o método find() para procurar todas as ocorrências da substring, como aqui:
# the_text = """A variation of the ordinary lorem ipsum
# text has been used in typesetting since the 1960s 
# or earlier, when it was popularized by advertisements 
# for Letraset transfer sheets. It was introduced to 
# the Information Age in the mid-1980s by the Aldus Corporation, 
# which employed it in graphics and word-processing templates
# for its desktop publishing program PageMaker (from Wikipedia)"""
#
# fnd = the_text.find('the')
# while fnd != -1:
#     print(fnd)
#     fnd = the_text.find('the', fnd + 1)
# 
# 
# O código imprime os índices de todas as ocorrências do artigo the, e o seu output é semelhante a este:
# 15
# 80
# 198
# 221
# 238
# 
# output
# 
# Há também uma mutação de três parâmetros do método find() - o terceiro argumento aponta para o primeiro index que não será tomado em consideração durante a pesquisa (na realidade é o limite superior da 
# pesquisa).
# 
# Veja o nosso exemplo abaixo:
# print('kappa'.find('a', 1, 4))
# print('kappa'.find('a', 2, 4))
#
#
# O segundo argumento especifica o index em que a pesquisa será iniciada (não tem de caber dentro da string).
# 
# Portanto, o exemplo modificado tem como output:
# 1
# -1
#
# output
# 
# (a não pode ser encontrado dentro dos limites de pesquisa indicados no segundo print().
#
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))