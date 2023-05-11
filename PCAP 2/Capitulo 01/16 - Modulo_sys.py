# O seu primeiro módulo: passo 11
#
# É altura de tornar o nosso exemplo mais complicado - até agora assumimos que o ficheiro Python principal está localizado na mesma pasta/diretoria que o módulo a ser importado.
#
# Vamos desistir desta suposição e realizar a seguinte experiência de pensamento:
#
#    estamos a utilizar Windows ® OS (esta suposição é importante, pois a forma do nome do ficheiro depende disso)
#    o script Python principal está em C:\Users\user\py\progs e é chamado main.py
#    o módulo a ser importado está localizado em C:\Users\user\py\modules 
#
# De que forma o Python procura módulos - árvore de acesso aos módulos
#
# Como lidar com isto?
#
# Para responder a esta pergunta, temos de falar sobre a forma como o Python procura módulos. Há uma variável especial (na realidade uma lista) que armazena todos os locais (pastas/diretorias) que são 
# pesquisados a fim de encontrar um módulo que tenha sido solicitado pela instrução de importação.
#
# O Python navega por estas pastas pela ordem em que estão listadas na lista - se o módulo não puder ser encontrado em nenhuma destas diretorias, a importação falha.
#
# Caso contrário, a primeira pasta contendo um módulo com o nome desejado será tomada em consideração (se alguma das restantes pastas contiver um módulo com esse nome, será ignorada).
#
# A variável é chamada path, e é acessível através do módulo chamado sys. É assim que se pode verificar o seu valor regular:
#

import sys

for p in sys.path:
    print(p)


# Lançámos o código dentro da pasta C:\User\user , e isto é o que obtivemos:
# C:\Users\user
# C:\Users\user\AppData\Local\Programs\Python\Python36-32\python36.zip
# C:\Users\user\AppData\Local\Programs\Python\Python36-32\DLLs
# C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib
# C:\Users\user\AppData\Local\Programs\Python\Python36-32
# C:\Users\user\AppData\Local\Programs\Python\Python36-32\lib\site-packages
#
# output de amostra
#
# Nota: a pasta em que a execução começa é listada no elemento do primeiro caminho.
#
# Nota mais uma vez: há um ficheiro zip listado como um dos elementos do caminho - não é um erro. O Python é capaz de tratar ficheiros zip como pastas normais - isto pode poupar muito armazenamento.
# 
# Consegue descobrir como podemos resolver o nosso problema agora? Podemos adicionar uma pasta contendo o módulo à variável path (é totalmente modificável).
