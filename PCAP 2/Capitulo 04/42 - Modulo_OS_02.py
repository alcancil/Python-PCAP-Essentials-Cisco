# Criar diretorias em Python
#
# O módulo os fornece uma função chamada mkdir, que, tal como o comando mkdir em Unix e Windows, permite criar uma diretoria. A função mkdir requer um caminho, que pode ser relativo ou absoluto. Recordemos 
# como são ambos os caminhos na prática:
#
#    my_first_directory — este é um caminho relativo que irá criar a diretoria my_first_directory na diretoria de trabalho atual;
#    ./my_first_directory — este é um caminho relativo que aponta explicitamente para a diretoria de trabalho atual. Tem o mesmo efeito que o caminho acima;
#    ../my_first_directory — este é um caminho relativo que criará a diretoria my_first_directory na diretoria pai da diretoria de trabalho atual;
#    /python/my_first_directory — este é o caminho absoluto que irá criar a diretoria my_first_directory, que por sua vez está na diretoria Python na diretoria de raiz.
#
# Veja o código no editor. Este mostra um exemplo de como criar a diretoria my_first_directory usando um caminho relativo. Esta é a variante mais simples do caminho relativo, que consiste em passar apenas o 
# nome da diretoria.
#
# Se testar o seu código aqui, ele produzirá a diretoria recém-criada ['my_first_directory'] (e todo o conteúdo do catálogo de trabalho atual).
#
# A função mkdir cria uma diretoria no caminho especificado. Note que a execução do programa duas vezes levantará um FileExistsError.
#
# Isto significa que não podemos criar uma diretoria se ela já existir. Para além do argumento path, a função mkdir pode opcionalmente tomar o argumento mode, que especifica as permissões de diretoria. No 
# entanto, em alguns sistemas, o argumento mode é ignorado.
#
# Para alterar as permissões de diretoria, recomendamos a função chmod, que funciona de forma semelhante ao comando chmod em sistemas Unix. Pode encontrar mais informações sobre o assunto na documentação.
#
# No exemplo acima, outra função fornecida pelo módulo os, chamada listdir, é utilizada. A função listdir devolve uma lista contendo os nomes dos ficheiros e diretorias que se encontram no caminho passado 
# como um argumento.
#
# Se nenhum argumento lhe for passado, será utilizada a diretoria de trabalho atual (como no exemplo acima). É importante que o resultado da função listdir omita as entradas '.' e '..', que são exibidas, por # exemplo, ao usar o comando ls -a em sistemas Unix.
#
# NOTA: No Windows e no Unix, há um comando chamado mkdir, que requer uma diretoria path. O equivalente ao código acima que cria a diretoria my_first_directory é o comando mkdir my_first_directory.
#

import os

os.mkdir("my_first_directory")
print(os.listdir())
