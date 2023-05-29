# Bytearrays: continuação
#
# Então, como escrevemos uma byte array para um ficheiro binário?
#
# Veja o código no editor. Vamos analisá-lo:
#
#    primeiro, inicializamos bytearray com valores subsequentes a partir de 10; se quiser que o conteúdo do ficheiro seja claramente legível, substitua 10 por algo como ord('a') - isto produzirá bytes 
# contendo valores correspondentes à parte alfabética do código ASCII (não pense que fará do ficheiro um ficheiro de texto - ainda é binário, pois foi criado com uma bandeira wb );
#    em seguida, criamos o ficheiro usando a função open() - a única diferença em comparação com as variantes anteriores é o modo aberto que contém a bandeira b ;
#    o método write() toma o seu argumento (bytearray) e envia-o (como um todo) para o ficheiro;
#    a stream é então fechada de forma rotineira.
#
# O método write() devolve uma série de bytes escritos com sucesso.
#
# Se os valores diferirem do comprimento dos argumentos do método, poderá anunciar alguns erros de escrita.
#
# Neste caso, não fizemos uso do resultado - isto pode não ser apropriado em todos os casos.
#
# Tente executar o código e analisar o conteúdo do ficheiro de output recém-criado.
#
# Vai utilizá-lo na próxima etapa.
#
# Como ler bytes de uma stream
#
# A leitura a partir de um ficheiro binário requer o uso de um nome de método especializado readinto(), uma vez que o método não cria um novo objeto de bytearray, mas preenche um previamente criado com os 
# valores retirados do ficheiro binário.
#
# Nota:
#
#    o método devolve o número de bytes lidos com sucesso;
#    o método tenta preencher todo o espaço disponível dentro do seu argumento; se houver mais dados no ficheiro do que espaço no argumento, a operação lida para antes do fim do ficheiro; caso contrário, o # resultado do método pode indicar que a bytearray só foi preenchida de forma fragmentada (o resultado mostrá-lo-á, também, e a parte do array que não está a ser utilizada pelo conteúdo recentemente lido 
# permanece intacta)
#
# Veja o código completo abaixo:
# from os import strerror
#
# data = bytearray(10)
#
# try:
#    bf = open('file.bin', 'rb')
#    bf.readinto(data)
#    bf.close()
#
#    for b in data:
#        print(hex(b), end=' ')
# except IOError as e:
#    print("I/O error occurred:", strerror(e.errno))
#
#
# Vamos analisá-lo:
#
#    primeiro, abrimos o ficheiro (aquele que criou utilizando o código anterior) com o modo descrito como rb;
#    em seguida, lemos seu conteúdo na bytearray chamada data, de tamanho dez bytes;
#    finalmente, imprimimos o conteúdo da bytearray - são os mesmos que você esperava?
#
# Execute o código e verifique se está a funcionar.

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))