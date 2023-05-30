# Onde estou agora?
#
# Já sabe como criar diretorias e como se mover entre elas. Pos vezes, quando se tem uma estrutura de diretorias muito grande por onde navegar, pode não se saber em que diretoria se está atualmente a 
# trabalhar.
#
# Programador perdido
#
#
# Como provavelmente adivinhou, o módulo os fornece uma função que devolve informação sobre a diretoria de trabalho atual. É chamada getcwd. Olhe para o código no editor para ver como a utilizar na prática.
#
# Resultado:
# .../my_first_directory
# .../my_first_directory/my_second_directory
#
# output
#
# No exemplo, criamos a diretoria my_first_directory e a diretoria my_second_directory dentro desta. Na passo seguinte, alteramos a diretoria de trabalho atual para a diretoria my_first_directory, e depois 
# exibimos a diretoria de trabalho atual (primeira linha do resultado).
#
# Em seguida, vamos para a diretoria my_second_directory e exibimos novamente a diretoria de trabalho atual (segunda linha do resultado). Como pode ver, a função getcwd devolve o caminho absoluto para as 
# diretorias.
#
# NOTA: Em sistemas semelhantes a Unix, o equivalente à função getcwd é o comando pwd, que imprime o nome da diretoria de trabalho atual.

import os

os.makedirs("meu_primeiro_diretorio/meu_segundo_diretorio")
os.chdir("meu_primeiro_diretorio")
print(os.getcwd())
os.chdir("meu_segundo_diretorio")
print(os.getcwd())