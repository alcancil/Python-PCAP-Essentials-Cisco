# Métodos em detalhe: continuação
#
# O parâmetro self é utilizado para obter acesso à instância do objeto e às variáveis de classe.
#
# O exemplo mostra as duas formas de utilizar self:
class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()


# Output do código:
# 2 3
#
# output
#
# A função self é também utilizado para invocar outros métodos objeto/classe de dentro da classe.
#
# Tal como aqui:

class Classy:
    def other(self):
        print("other")

    def method(self):
        print("method")
        self.other()


obj = Classy()
obj.method()


# Output do código:
# method
# other