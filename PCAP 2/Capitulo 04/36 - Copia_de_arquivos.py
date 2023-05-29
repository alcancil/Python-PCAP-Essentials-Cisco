# Cópia de ficheiros - uma ferramenta simples e funcional
#
# Agora vai amalgamar todos estes novos conhecimentos, adicionar-lhe alguns elementos novos, e utilizá-los para escrever um código real que seja capaz de copiar efetivamente o conteúdo de um ficheiro.
#
# Claro que o objetivo não é fazer um melhor substituto para comandos como copy (MS Windows) ou cp (Unix/Linux), mas ver uma forma possível de criar uma ferramenta de trabalho, mesmo que ninguém a queira 
# utilizar.
#
# Veja o código no editor. Vamos analisá-lo:
#
#    linhas 3 a 8: pedir ao utilizador o nome do ficheiro a copiar, e tentar abri-lo para ler; terminar a execução do programa se a abertura falhar; nota: utilizar a função exit() para parar a execução do 
# programa e para passar o código de conclusão para o SO; qualquer código de conclusão que não 0 diz que o programa encontrou alguns problemas; use o valor errno para especificar a natureza do problema;
#    linhas 10 a 16: repetir quase a mesma ação, mas desta vez para o ficheiro de output;
#    linha 18: preparar um pedaço de memória para transferir dados do source file para o ficheiro alvo; essa área de transferência é muitas vezes chamada de buffer, daí o nome da variável; o tamanho do buffer # é arbitrário - neste caso, decidimos usar 64 kilobytes; tecnicamente, um buffer maior é mais rápido a copiar itens, pois um buffer maior significa menos operações I/O; na verdade, há sempre um limite, cujo # cruzamento não traz mais melhorias; teste-o você mesmo se quiser.
#    linha 19: contar os bytes copiados - este é o contador e o seu valor inicial;
#    linha 21: tentar preencher o buffer pela primeira vez;
#    linha 22: desde que se obtenha um número não nulo de bytes, repetir as mesmas ações;
#    linha 23: escrever o conteúdo do buffer no ficheiro de output (nota: utilizámos uma slice para limitar o número de bytes a escrever, uma vez que write() prefere sempre escrever todo o buffer)
#    linha 24: atualizar o contador;
#    linha 25: ler o próximo pedaço de ficheiro;
#    linhas 30 a 32: alguma limpeza final - o trabalho está feito.


from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()