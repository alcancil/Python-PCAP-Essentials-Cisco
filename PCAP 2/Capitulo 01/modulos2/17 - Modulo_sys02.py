# O seu primeiro módulo: passo 12
#
# Uma das várias soluções possíveis parece-se com esta:
# Atualizar o ficheiro main.py com path.append('..\\modules')

from sys import path

path.append('..\\modulos2')

import modulo03

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(modulo03.suml(zeroes))
print(modulo03.prodl(ones))


# Nota:
#
#    duplicámos o \ nome da pasta interna - sabe porquê?
#
# Porque uma barra invertida é usada para escapar a outros carateres - se quiser obter apenas uma barra invertida, tem de a escapar.
#
# usámos o nome relativo da pasta - isto funcionará se iniciar o ficheiro main.py diretamente da sua home folder, e não funcionará se a diretoria atual não se ajustar ao caminho relativo; pode sempre usar um # caminho absoluto, como este:
#
# path.append('C:\\Users\\user\\py\\modules')
#
#
# utilizámos o método append() - com efeito, o novo caminho ocupará o último elemento da lista de caminhos; se não gostar da ideia, pode usar insert() em vez disso.

