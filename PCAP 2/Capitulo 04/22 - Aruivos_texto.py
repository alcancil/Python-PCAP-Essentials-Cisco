# Processamento de ficheiros de texto: continuação
#
# Se tem a certeza absoluta de que o comprimento do ficheiro é seguro e pode ler todo o ficheiro para a memória de uma só vez, pode fazê-lo - a função read() , invocada sem quaisquer argumentos ou com um 
# argumento que avalia None, vai fazer o trabalho por si.
#
# Lembre-se - a leitura de um ficheiro de um terabyte usando este método pode corromper o seu sistema operativo.
#
# Não espere milagres - a memória do computador não é esticável.
#
# Veja o código no editor. O que pensa disto?
#
# Vamos analisá-lo:
#
#    abra o ficheiro como anteriormente;
#    leia o seu conteúdo através de uma invocação da função read() ;
#    em seguida, processe o texto, iterando através dele com um loop for , e atualizando o valor do contador a cada turno do loop;


from os import strerror

try:
    cnt = 0
    s = open('21-text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))