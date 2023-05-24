# Como o Python encontra propriedades e métodos: continuação
#
# O mesmo efeito pode ser observado com variáveis de instância - veja o segundo exemplo no editor.
#
# O construtor de classe Sub cria uma variável de instância chamada subVar, enquanto o construtor Super faz o mesmo com uma variável chamada supVar. Como anteriormente, ambas as variáveis são acessíveis de 
# dentro do objeto da classe Sub.
#
# O output do programa é:
# 12
# 11
#
# output
#
# Nota: a existência da variável supVar é obviamente condicionada pela invocação do construtor de classe Super . Omiti-la resultaria na ausência da variável no objeto criado (experimente-o você mesmo)

# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)