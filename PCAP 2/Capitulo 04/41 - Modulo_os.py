# Obter informações sobre o sistema operativo
#
# Antes de criar a sua primeira estrutura de diretoria, verá como pode obter informações sobre o sistema operativo atual. Isto é realmente fácil porque o módulo os fornece uma função chamada uname, que 
# devolve um objeto contendo os seguintes atributos:
#
#    systemname — armazena o nome do sistema operativo;
#    nodename — armazena o nome da máquina na network;
#    release — armazena o lançamento do sistema operativo;
#    version — armazena a versão do sistema operativo;
#    machine — armazena o identificador de hardware, por exemplo, x86_64.
#
# Vejamos como é na prática:
#
# Em distros Linux
# import os
# print(os.uname())

# Resultado:
# posix.uname_result(sysname='Linux', nodename='192d19f04766', release='4.4.0-164-generic', version='#192-Ubuntu SMP Fri Sep 13 12:02:50 UTC 2019', machine='x86_64')
#
# output
#
# Como pode ver, a função uname devolve um objeto contendo informações sobre o sistema operativo. O código acima foi lançado em Ubuntu 16.04.6 LTS, por isso não se surpreenda se obtiver um resultado 
# diferente, porque depende do seu sistema operativo.
#
# Infelizmente, a função uname só funciona em alguns sistemas Unix. Se utilizar o Windows, pode usar a função uname no módulo platform, que devolve um resultado semelhante.
#
# O módulo os permite-lhe distinguir rapidamente o sistema operativo utilizando o atributo name, que suporta um dos seguintes nomes:
#
#     posix — obterá este nome se utilizar Unix;
#     nt — obterá este nome se utilizar o Windows;
#     java — obterá este nome se o seu código estiver escrito em Jython.
#
# Para o Ubuntu 16.04.6 LTS, o atributo name devolve o nome posix:
#

import os
print(os.name)

# Resultado:
# posix
#
# output
#
# NOTA: Em sistemas Unix, existe um comando chamado uname que devolve as mesmas informações (se o executar com a opção -a) que a função uname.

