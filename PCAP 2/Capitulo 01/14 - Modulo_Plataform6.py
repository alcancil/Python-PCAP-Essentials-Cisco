# Funções selecionadas a partir do módulo platform : continuação
#
# As funções python_implementation e python_version_tuple .
#
# Se precisar de saber qual a versão do Python que está a executar o seu código, pode verificá-la utilizando várias funções dedicadas - aqui estão duas delas:
#
#    python_implementation() → devolve uma string denotando a implementação do Python (esperar CPython aqui, a menos que decida utilizar qualquer ramo de Python não canónico)
#
#    python_version_tuple() → devolve um tuple de três elementos preenchido com:
#        a parte principal da versão do Python
#        a parte secundária;
#        o número do patch level.
#
# O nosso programa de exemplo produziu o seguinte output:
# CPython
# 3
# 7
# 7
#
# output de amostra
#
# É muito provável que a sua versão do Python seja diferente.

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)