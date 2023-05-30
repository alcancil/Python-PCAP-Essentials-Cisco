
# Key takeaways
#
# 1. A função uname devolve um objeto que contém informação sobre o sistema operativo atual. O objeto tem os seguintes atributos:
#
#    systemname (armazena o nome do sistema operativo)
#    nodename (armazena o nome da máquina na rede)
#    release (armazena a versão do sistema operativo)
#    version (armazena a versão do sistema operativo)
#    machine (armazena o identificador de hardware, por exemplo x86_64.)
#
# 2. O atributo name disponível no módulo os permite distinguir o sistema operativo. Devolve um dos três valores seguintes:
#
    posix (receberá este nome se usar Unix)
    nt (receberá este nome se usar o Windows)
    java (receberá este nome se o seu código estiver escrito em algo como Jython)

3. Os loops mkdir cria uma diretoria no caminho percorrido como seu argumento. O caminho pode ser relativo ou absoluto, por exemplo
import os

os.mkdir("hello") # the relative path
os.mkdir("/home/python/hello") # the absolute path


Nota: Se a diretoria existir, uma exceção FileExistsError será lançada. Além da função mkdir , o módulo os fornece a função makedirs , que permite criar recursivamente todas as diretorias num caminho.

4. O resultado da função listdir() é uma lista contendo os nomes dos ficheiros e diretorias que se encontram no caminho percorrido como seu argumento.

É importante lembrar que a função listdir omite as entradas '.' e '..', que são exibidas, por exemplo, quando se utiliza o comando ls -a em sistemas Unix. Se o caminho não for passado, o resultado será devolvido para a diretoria de trabalho atual.

5. Para se deslocar entre diretorias, pode usar uma função chamada chdir(), que altera a diretoria de trabalho atual para o caminho especificado. Como seu argumento, toma qualquer caminho relativo ou absoluto.

Se quiser descobrir qual é a diretoria de trabalho atual, pode utilizar a função getcwd() , que lhe devolve o caminho.

6. Para remover uma diretoria, pode utilizar a função rmdir() , mas, para remover uma diretoria e as suas subdiretorias, utilize a função removedirs() .

7. Tanto no Unix como no Windows, pode usar a função do sistema, que executa um comando passado a ele como uma string, por exemplo:
import os

returned_value = os.system("mkdir hello")


A função do sistema no Windows devolve o valor devolvido pela shell após executar o comando dado, enquanto que no Unix devolve o estado de saída do processo.



Exercício 1

Qual é o output do seguinte snippet se o executar no Unix?

import os
print(os.name)

posix


Exercício 2

Qual é o output do seguinte snippet?

import os

os.mkdir("hello")
print(os.listdir())

['hello']


