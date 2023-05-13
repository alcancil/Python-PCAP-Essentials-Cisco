# Os loops center() .
# 
# A variante de um parâmetro do método center() faz uma cópia da string original, tentando centralizá-la dentro de um campo de uma largura especificada.
# 
# A centralização é realmente feita adicionando alguns espaços antes e depois da string.
# 
# Não espere que este método demonstre quaisquer competências sofisticadas. É bastante simples.
# 
# O exemplo no editor usa parêntesis retos para mostrar claramente onde começa e termina a string centrada.
# 
# O seu output é o seguinte:
# [  alpha   ]
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')

# output
#
# Se o comprimento do campo alvo for demasiado pequeno para caber na string, a string original é devolvida.
# 
# Pode ver o método center() em mais exemplos aqui:
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
# 
#
# Execute os snippets acima e verifique qual o output que eles produzem.
# 
# A variante de dois parâmetros de center() faz uso do caratere do segundo argumento, em vez de um espaço. Analise o exemplo abaixo:
print('[' + 'gamma'.center(20, '*') + ']')
# 
#
# É por isso que o output agora se assemelha a este:
# [*******gamma********]
#
# output
#
# Realize mais experiências.