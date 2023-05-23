# Métodos em detalhe
#
# Vamos resumir todos os factos relativos à utilização de métodos em classes Python.
#
# Como já sabe, um método é uma função incorporada dentro de uma classe.
#
# Existe um requisito fundamental - um método é obrigado a ter pelo menos um parâmetro (não existem métodos sem parâmetros - um método pode ser invocado sem argumento, mas não declarado sem parâmetros).
#
# O primeiro (ou único) parâmetro é geralmente chamado self. Sugerimos que siga a convenção - é normalmente usada, e causará algumas surpresas ao usar outros nomes para a mesma.
#
# O nome self sugere a finalidade do parâmetro - identifica o objeto para o qual o método é invocado.
#
# Se vai invocar um método, não deve passar o argumento para o parâmetro self - o Python irá configurá-lo por si.
#
# O exemplo no editor mostra a diferença.
#

class Classy:
    def method(self):
        print("method")


obj = Classy()
obj.method()



# Output do código:
# method
# 
# output
# 
# Note a forma como criámos o objeto - tratámos o nome da classe como uma função, devolvendo um objeto recentemente instanciado da classe.
# 
# Se quiser que o método aceite outros parâmetros self, deve:
#
#    colocá-los depois de self na definição do método;
#    entregá-los durante a invocação sem especificar self (como anteriormente)
# 
# Tal como aqui:
class Classy:
    def method(self, par):
        print("method:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)


# Output do código:
# method: 1
# method: 2
# method: 3

