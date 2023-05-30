# Criação de diretoria recursiva
#
# A função mkdir é muito útil, mas e se precisar de criar outra diretoria na diretoria que acabou de criar? Obviamente, pode ir à diretoria criada e criar outra diretoria dentro dela, mas felizmente o módulo # os fornece uma função chamada makedirs, o que torna esta tarefa mais fácil.
#
# A função makedirs permite a criação de diretoria recursiva, o que significa que todas as diretorias no caminho serão criadas. Vamos olhar para o código no editor e ver como ele é na prática.
#
# O código deve produzir o seguinte resultado:
# ['my_second_directory']
#
# output
#
# O código cria duas diretorias. A primeira delas é criada na diretoria de trabalho atual, enquanto a segunda é criada na diretoria my_first_directory.
#
# Não tem de ir à diretoria my_first_directory para criar a diretoria my_second_directory, porque a função makedirs faz isto por si. No exemplo acima, vamos à diretoria my_first_directory para mostrar que o 
# comando makedirs cria a subdiretoria my_second_directory.
#
# Para se mover entre diretorias, pode usar uma função chamada chdir, que altera a diretoria de trabalho atual para o caminho especificado. Como argumento, toma qualquer caminho relativo ou absoluto. No nosso # exemplo, passámos-lhe o nome da primeira diretoria.
#
# NOTA: O equivalente à função makedirs nos sistemas Unix é o comando mkdir com o sinalizador -p, enquanto no Windows é simplesmente o comando mkdir com o caminho:
#
#    Sistemas semelhantes a Unix:
#
#    mkdir -p my_first_directory/my_second_directory
#
#    Windows:
#
#    mkdir my_first_directory/my_second_directory

import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())