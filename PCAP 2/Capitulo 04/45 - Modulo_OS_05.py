# Eliminar diretorias em Python
#
# O módulo os também permite eliminar diretorias. Dá-lhe a opção de eliminar uma única diretoria ou uma diretoria com as suas subdiretorias. Para eliminar uma única diretoria, pode-se utilizar uma função 
# chamada rmdir, que toma o caminho como seu argumento. Veja o código no editor.

import os

os.mkdir("dir01")
print(os.listdir())
os.rmdir("dir01")
print(os.listdir())


# O exemplo acima é realmente simples. Primeiro, a diretoria my_first_directory é criada e, em seguida, é removida utilizando-se a função rmdir. A função listdir é usada como prova de que a diretoria foi 
# removida com sucesso. Neste caso, devolve uma lista vazia. Ao eliminar uma diretoria, certifique-se de que esta existe e está vazio, caso contrário será levantada uma exceção.
#
# Para remover uma diretoria e as suas subdiretorias, pode utilizar a função removedirs , o que requer que se especifique um caminho contendo todas as diretorias que devem ser removidos:
#

import os

os.makedirs("dir03/dir04")
os.removedirs("dir03/dir04")
print(os.listdir())

# Tal como com a função rmdir, se uma das diretorias não existir ou não estiver vazia, será levantada uma exceção.
#
# NOTA: No Windows e no Unix existe um comando chamado rmdir, que, tal como a função rmdir, remove diretorias. Além disso, ambos os sistemas têm comandos para eliminar uma diretoria e o seu conteúdo. No Unix, # este é o comando rm com o sinalizador -r.