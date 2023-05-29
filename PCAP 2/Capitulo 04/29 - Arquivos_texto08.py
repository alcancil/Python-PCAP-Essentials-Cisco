# Lidar com ficheiros de texto: continuação
#
# Veja o exemplo no editor. Modificámos o código anterior para escrever linhas inteiras no ficheiro de texto.
#
# O conteúdo do ficheiro recentemente criado é o mesmo.
#
# Nota: pode usar o mesmo método para escrever para o stream stderr , mas não tente abri-lo, pois está sempre aberto implicitamente.
#
# Por exemplo, se quiser enviar uma string de mensagem para stderr para o distinguir do output normal de programa, pode ter este aspeto:
# import sys
# sys.stderr.write("Error message")

from os import strerror

try:
    fo = open('30-newtext.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
