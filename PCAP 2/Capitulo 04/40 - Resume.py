
Key takeaways

1. Para ler o conteúdo de um ficheiro, podem ser utilizados os seguintes métodos de stream:

    read(number) — lê os carateres/bytes number do ficheiro e devolve-os como uma string; é capaz de ler o ficheiro inteiro de uma só vez;
    readline() — lê uma única linha do ficheiro de texto;
    readlines(number) — lê as linhas number do ficheiro de texto; é capaz de ler todas as linhas ao mesmo tempo;
    readinto(bytearray) — lê os bytes do ficheiro e preenche o bytearray com eles;


2. Para escrever novos conteúdos num ficheiro, podem ser utilizados os seguintes métodos de stream:

    write(string) — escreve um string para um ficheiro de texto;
    write(bytearray) — escreve todos os bytes de bytearray para um ficheiro;


3. Os loops open() devolve um objeto iterável que pode ser utilizado para iterar através de todas as linhas do ficheiro dentro de um loop for . Por exemplo:
for line in open("file", "rt"):
    print(line, end='')


O código copia o conteúdo do ficheiro para a consola, linha a linha. Nota: o stream fecha-se automaticamente quando chega ao fim do ficheiro.

Exercício 1

O que esperamos do método readlines() quando o stream está associado a um ficheiro vazio?

Uma lista vazia (uma lista de comprimento zero).


Exercício 2

O que se pretende fazer com o seguinte código?
for line in open("file", "rt"):
    for char in line:
        if char.lower() not in "aeiouy ":
            print(char, end='')


Copia o conteúdo do ficheiro para a consola, ignorando todas as vogais.


Exercício 3

Vai processar um bitmap armazenado num ficheiro com o nome image.png, e deseja ler o seu conteúdo como um todo numa variável de bytearray chamada image. Adicione uma linha ao seguinte código para atingir este objetivo.
try:
    stream = open("image.png", "rb")
    # Insert a line here.
    stream.close()
except IOError:
    print("failed")
else:
    print("success")


image = bytearray(stream.read())

