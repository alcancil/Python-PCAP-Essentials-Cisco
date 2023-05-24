# Como o Python encontra propriedades e métodos: continuação
#
# Vamos tentar fazer algo semelhante, mas com propriedades (mais precisamente: com variáveis de classe).
#
# Dê uma vista de olhos no exemplo no editor.
#
# Como pode ver, a classe Super define uma variável de classe chamada supVar, e a classe Sub define uma variável chamada subVar.
#
# Ambas as variáveis são visíveis dentro do objeto da classe Sub - é por isso que o código faz o output:
# 2
# 1

# Testing properties: class variables.
class Super:
    supVar = 1


class Sub(Super):
    subVar = 2


obj = Sub()

print(obj.subVar)
print(obj.supVar)
