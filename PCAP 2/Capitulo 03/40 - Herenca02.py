# Herança - porquê e como?
#
# Quando o Python precisa que qualquer classe/objeto seja apresentado como uma string (colocar um objeto como argumento na invocação de função print() encaixa-se nesta condição) ele tenta invocar um método 
# chamado __str__() do objeto e usar a string que ele devolve.
#
# O método por defeito __str__() devolve a string anterior - feia e não muito informativa. Pode alterá-lo apenas definindo o seu próprio método do nome.
#
# Acabámos de fazer isso - veja o código no editor.
#
# Este novo método __str__() faz uma string consistindo nos nomes da estrela e da galáxia - nada de especial, mas os resultados da impressão parecem melhores agora, certo?
#
# Consegue adivinhar o output? Execute o código para verificar se estava certo.

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)
