# A vida interior das classes e objetos: continuação
#
# __module__ é também uma string - armazena o nome do módulo que contém a definição da classe.
#
# Vamos verificá-la - execute o código no editor.
#
# Output do código:
# __main__
# __main__
#
# output
#
# Como sabe, qualquer módulo chamado __main__ não é na realidade um módulo, mas o ficheiro atualmente em execução.
#
class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)