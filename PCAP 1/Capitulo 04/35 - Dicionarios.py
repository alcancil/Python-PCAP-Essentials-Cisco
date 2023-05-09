
# O que é um dicionário?
# 
# O dicionário é outra estrutura de dados Python. Não é um tipo de sequência (mas pode ser facilmente adaptado ao processamento de sequências) e é mutável.
#
# Para explicar o que é realmente o dicionário Python, é importante compreender que se trata literalmente de um dicionário.
#
# O dicionário Python funciona da mesma forma que um dicionário bilingue. Por exemplo, tem uma palavra inglesa (por exemplo, cat) e precisa do seu equivalente francês. Navega no dicionário para encontrar a # palavra (pode usar diferentes técnicas para o fazer - não importa) e eventualmente obtém-na. A seguir, verifica o homólogo francês e é (muito provavelmente) a palavra "chat".
# Conceito de tuples vs. dicionários
#
# No mundo de Python, a palavra que se procura chama-se key. A palavra que obtém do dicionário chama-se um value.
#
# Isto significa que um dicionário é um conjunto de pares de key-values (valores-chave). Nota:
#
#    cada chave deve ser única - não é possível ter mais do que uma chave com o mesmo valor;
#    uma chave pode ser qualquer tipo de objeto imutável: pode ser um número (inteiro ou float), ou mesmo uma string, mas não uma lista;
#    um dicionário não é uma lista - uma lista contém um conjunto de valores numerados, enquanto que um dicionário contém pares de valores;
#    a função len() funciona também para dicionários - devolve o número de elementos de key-value no dicionário;
#    um dicionário é uma ferramenta de sentido único - se tiver um dicionário inglês-francês, pode procurar por equivalentes franceses de termos ingleses, mas não vice-versa. 
#
# Agora podemos mostrar-lhe alguns exemplos de trabalho.
#
# Como fazer um dicionário?
#
# Se quiser atribuir alguns pares iniciais a um dicionário, deverá utilizar a seguinte sintaxe:

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#
# No primeiro exemplo, o dicionário usa chaves e valores que são ambas strings. No segundo, as chaves são strings, mas os valores são inteiros. A disposição inversa (teclas → números, valores → strings) 
# também é possível, bem como a combinação número-número.
#
# A lista de pares é rodeada por chavetas, enquanto os pares em si são separados por vírgulas, e as chaves e valores por dois pontos.
#
# O primeiro dos nossos dicionários é um dicionário inglês-francês muito simples. O segundo - uma diretoria telefónica muito pequena.
#
# Os dicionários vazios são construídos por um par vazio de chavetas - nada de invulgar.
#
# O dicionário como um todo pode ser impresso com uma única invocação print() . O snippet pode produzir o seguinte output:
# {'dog': 'chien', 'horse': 'cheval', 'cat': 'chat'}
# {'Suzy': 5557654321, 'boss': 5551234567}
# {}
#
# output
#
# Notou alguma coisa surpreendente? A ordem dos pares impressos é diferente do que na atribuição inicial. O que é que isso significa?
#
# Em primeiro lugar, é uma confirmação de que os dicionários não são listas - não preservam a ordem dos seus dados, uma vez que a ordem não tem qualquer significado (ao contrário do que acontece nos 
# dicionários de papel reais). A ordem em que um dicionário armazena os seus dados está completamente fora do seu controlo, e das suas expectativas. Isso é normal. (*)
#
# NOTA
#
# (*) Em Python 3.6x os dicionários tornaram-se coleções ordenadas por defeito. Os seus resultados podem variar dependendo da versão Python que estiver a utilizar.