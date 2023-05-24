# Como o Python encontra propriedades e métodos: continuação
#
# A herança múltipla ocorre quando uma classe tem mais de uma superclasse. Sintaticamente, tal herança é apresentada como uma lista separada por vírgulas de superclasses colocadas dentro de parêntesis, após o # novo nome da classe - tal como aqui:
class SuperA:
    var_a = 10
    def fun_a(self):
        return 11


class SuperB:
    var_b = 20
    def fun_b(self):
        return 21


class Sub(SuperA, SuperB):
    pass

obj = Sub()

print(obj.var_a, obj.fun_a())
print(obj.var_b, obj.fun_b())


# A classe Sub tem duas superclasses: SuperA e SuperB. Isto significa que a classe Sub herda todos os bens oferecidos por ambos SuperA e SuperB.
#
# O código imprime:
# 10 11
# 20 21
#
# output
#
# Agora é tempo de introduzir um termo completamente novo - overriding.
#
# O que pensa que acontecerá se mais do que uma das superclasses definir uma entidade com um determinado nome?