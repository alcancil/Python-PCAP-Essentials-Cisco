# Como ler bytes de uma stream: continuação
#
# Se o método read() é invocado com um argumento, especifica o número máximo de bytes a serem lidos.
#
# O método tenta ler o número desejado de bytes do ficheiro, e o comprimento do objeto devolvido pode ser utilizado para determinar o número de bytes efetivamente lidos.
#
# Pode usar o método tal como aqui:

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Nota: os primeiros cinco bytes do ficheiro foram lidos pelo código - os cinco seguintes ainda estão à espera de ser processados.