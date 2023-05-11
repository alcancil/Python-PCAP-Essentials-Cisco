
# Key takeaways
#
# 1. Uma função chamada dir() pode mostrar-lhe uma lista das entidades contidas dentro de um módulo importado. Por exemplo:
# import os
# dir(os)
#
#
# imprime a lista de todas as facilidades do módulo os que pode utilizar no seu código.
#
# 2. O método math acopla mais de 50 símbolos (funções e constantes) que realizam operações matemáticas (como sine(), pow(), factorial()) ou fornecendo valores importantes (como π e o símbolo de Euler e).
#
# 3. Os loops random agrupa mais de 60 entidades concebidas para o ajudar a utilizar números pseudo-aleatórios. Não se esqueça do sufixo "aleatório", pois não existe um número verdadeiramente aleatório # # # quando se trata de os gerar utilizando os algoritmos do computador.
#
# 4. O objeto da exceção platform contém cerca de 70 funções que lhe permitem mergulhar nas camadas inferiores do SO e hardware. A sua utilização permite-lhe saber mais sobre o ambiente em que o seu código # é executado.
#
# 5. O Python Module Index (https://docs.python.org/3/py-modindex.html é uma diretoria de módulos disponíveis no universo Python, dirigido pela comunidade. Se quiser encontrar um módulo adequado às suas 
# necessidades, inicie aí a sua pesquisa.
#
#
# Exercício 1
#
# Qual é o valor esperado da variável result após o seguinte código ter sido executado?
import math
result = math.e == math.exp(1)
print(result)

#
# True
#
# Exercício 2
#
# (Complete a frase) Definir a seed do gerador com o mesmo valor cada vez que o seu programa é executado garante que...
# 
# ... os valores pseudo-aleatórios emitidos a partir do módulo random sejam exatamente os mesmos.
#
#
# Exercício 3
#
# Qual das funções do módulo platform irá utilizar para determinar o nome da CPU em execução dentro do seu computador?
#
# A função processor() .
#
#
# Exercício 4
#
# Qual é o output do seguinte snippet?
import platform

print(len(platform.python_version_tuple()))


# 3
