
Key takeaways

1. Um ficheiro tem de estar aberto antes de poder ser processado por um programa, e deve estar fechado quando o processamento estiver terminado.

A abertura do ficheiro associa-o ao stream, que é uma representação abstrata dos dados físicos armazenados na media. A forma como o stream é processado é chamada modo aberto. Existem três modos abertos:

    modo de leitura — apenas são permitidas operações de leitura;
    modo de escrita — apenas são permitidas operações de escrita;
    modo de update — tanto as escritas como as leituras são permitidas.


2. Dependendo do conteúdo do ficheiro físico, diferentes classes de Python podem ser utilizadas para processar ficheiros. Em geral, o BufferedIOBase é capaz de processar qualquer ficheiro, enquanto TextIOBase é uma classe especializada dedicada ao processamento de ficheiros de texto (ou seja, ficheiros contendo textos visíveis para humanos, divididos em linhas utilizando marcadores de nova linha). Assim, os streams podem ser divididos em binários e de texto.

3. A seguinte sintaxe da função open() é utilizada para abrir um ficheiro:

open(file_name, mode=open_mode, encoding=text_encoding)

A invocação cria um objeto de fluxo e associa-o ao ficheiro com o nome file_name, usando o especificado open_mode e definindo o especificado text_encoding, ou levanta uma exceção no caso de um erro.

4. Três streams predefinidos já estão abertos quando o programa é iniciado:

    sys.stdin — standard input;
    sys.stdout — standard output;
    sys.stderr — standard error output.


4. O objeto da exceção IOError , criado quando qualquer operação de ficheiro falha (incluindo operações abertas), contém uma propriedade chamada errno, que contém o código de conclusão da ação falhada. Use este valor para diagnosticar o problema.


Exercício 1

Como codificar o valor do argumento open() da função mode se for criar um novo ficheiro de texto para o preencher apenas com um artigo?

"wt" ou "w"


Exercício 2

Qual é o significado do valor representado por errno.EACESS?

Permissão negada: não tem permissão para aceder ao conteúdo do ficheiro.


Exercício 3

Qual é o output esperado do código seguinte, supondo que o ficheiro nomeado file não existe?
import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")


absent
