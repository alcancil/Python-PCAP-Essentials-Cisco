# Listas em ação
# Deixemos as listas de lado por um breve momento e vejamos uma questão intrigante.
#
# Imagine que precisa de reorganizar os elementos de uma lista, ou seja, inverter a ordem dos elementos: # o primeiro e o quinto, bem como o segundo e o quarto elementos serão trocados. O terceiro permanecerá # intocado.
#
#
# Pergunta: como se pode trocar os valores de duas variáveis?
#
# Veja o snippet:
#
# variable_1 = 1
# variable_2 = 2
#
# variable_2 = variable_1
# variable_1 = variable_2
# 
# 
# Se fizer algo como isto, perderá o valor previamente armazenado em variable_2. Alterar a ordem das 
# atribuições não ajudará. É necessária uma terceira variável que sirva como armazenamento auxiliar.
#
# É assim que se pode fazer:
# 
# variable_1 = 1
# variable_2 = 2
#
# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary
#
#
# O Python oferece uma forma mais conveniente de fazer a troca - veja:
#
# variable_1 = 1
# variable_2 = 2
#
# variable_1, variable_2 = variable_2, variable_1
#
#
# Claro, eficaz e elegante - não é?
#
# EX:
#

var1 = 1
var2 = 2

print("\nOrdem original: ", var1, var2)
var1, var2 = var2, var1
print("\nOrdem invertida: ", var1, var2) 