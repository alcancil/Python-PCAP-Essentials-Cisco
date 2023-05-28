# Processamento de ficheiros de texto: continuação
#
# A leitura do conteúdo de um ficheiro de texto pode ser feita usando vários métodos diferentes - nenhum deles é melhor ou pior do que qualquer outro. Depende de si qual deles prefere e gosta.
#
# Alguns deles serão por vezes mais práticos, e por vezes mais problemáticos. Seja flexível. Não tenha medo de mudar as suas preferências.
#
# O mais básico destes métodos é o que é oferecido pela função read() , que foi capaz de ver em ação na lição anterior.
#
# Se aplicada a um ficheiro de texto, a função é capaz de:
#
#    ler um número desejado de carateres (incluindo apenas um) do ficheiro, e devolvê-los como uma string;
#    ler todo o conteúdo do ficheiro, e devolvê-lo como uma string;
#    se não houver mais nada para ler (a cabeça de leitura virtual chega ao fim do ficheiro), a função devolve uma string vazia.
#
#
# Começaremos com a variante mais simples e utilizaremos um ficheiro com o nome text.txt. O ficheiro tem o seguinte conteúdo:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
#
# text.txt
#
# Vejamos agora o código no editor, e vamos analisá-lo.
#
# A rotina é bastante simples:
#
#    utilizar o mecanismo try-except e abrir o ficheiro do nome pré-determinado (text.txt no nosso caso)
#    tentar ler o primeiro caratere do ficheiro (ch = s.read(1))
#    se for bem sucedido (isto é comprovado por um resultado positivo da verificação do estado while ), fazer output do caratere (note o argumento end= - é importante! Não se quer saltar para uma nova linha 
# depois de cada caratere!);
#    atualizar o contador (cnt), também;
#    tentar ler o próximo caratere, e o processo repete-se.
#

from os import strerror

try:
    cnt = 0
    s = open('21-text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
