# Neste exemplo criamos uma pasta contendo um arquivo do codigo principal ( main.py ) e os seus respectivos modulos. Nesse arquivo vamos somente importas os modulos 1 e 2
# Quando realizamos a importação dos modulos, o proprio python cria uma pasta de cache contendo as instruções para que ele mesmo possa acessa - lo.
# OBS: Podemos dizer que:
#
#    quando se executa diretamente um ficheiro, a sua variável __name__ é definida como __main__;
#    quando um ficheiro é importado como um módulo, a sua variável __name__ é definida como o nome do ficheiro (excluindo .py)


import modulo, modulo02