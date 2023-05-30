# A função system()
#
# Todas as funções apresentadas nesta parte do curso podem ser substituídas por uma função chamada system, que executa um comando que lhe é passado como uma string.
#
# A função system está disponível tanto no Windows como no Unix. Dependendo do sistema, ela devolve um resultado diferente.
#
# No Windows, devolve o valor retornado pela shell após executar o comando dado, enquanto que no Unix devolve o estado de exit do processo.
#
# Vamos olhar para o código no editor e ver como ele é na prática.
#
# Resultado:
# 0
#
# output
#
# O exemplo acima funcionará tanto no Windows como no Unix. No nosso caso, recebemos o exit status 0, o que indica sucesso em sistemas Unix.
#
# Isto significa que a diretoria my_first_directory foi criada. Como parte do exercício, tente listar o conteúdo da diretoria onde criou a diretoria my_first_directory.

import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
