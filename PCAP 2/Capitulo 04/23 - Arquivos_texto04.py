# Processamento de ficheiros de texto: readline()
#
# Se quiser tratar o conteúdo do ficheiro como um conjunto de linhas e não como um monte de carateres, o método readline() irá ajudá-lo com isso.
#
# O método tenta ler uma linha completa de texto do ficheiro, e devolve-a como uma string em caso de sucesso. Caso contrário, ele devolve uma string vazia.
#
# Isto abre novas oportunidades - agora também se podem contar linhas facilmente, não apenas carateres.
#
# Vamos fazer uso disso. Veja o código no editor.
#
# Como se pode ver, a ideia geral é exatamente a mesma que nos dois exemplos anteriores.
#

from os import strerror

try:
    ccnt = lcnt = 0
    s = open('21-text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))