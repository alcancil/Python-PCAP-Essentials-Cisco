# Como ler bytes de uma stream
#
# Uma forma alternativa de ler o conteúdo de um ficheiro binário é oferecida pelo método denominado read().
#
# Invocado sem argumentos, tenta ler todo o conteúdo do ficheiro na memória, tornando-os parte de um objeto recentemente criado da classe bytes.
#
# Esta classe tem algumas semelhanças com bytearray, com exceção de uma diferença significativa - é imutável.
#
# Felizmente, não existem obstáculos à criação de uma byte array tirando o seu valor inicial diretamente do objeto de bytes, tal como aqui:

from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Tenha cuidado - não utilize este tipo de leitura se não tiver a certeza de que o conteúdo do ficheiro se adequa à memória disponível.
