# Passagem de parâmetros posicionais
# Uma técnica que atribui o iésimo (primeiro, segundo, e assim por diante) argumento ao iésimo (primeiro, segundo, e assim por diante) parâmetro de função é chamada passagem de parâmetro posicional, enquanto # os argumentos passados desta forma são denominados argumentos posicionais.
# 
# Já o usou, mas o Python pode oferecer muito mais. Vamos agora falar-lhe sobre isso.
#
# def my_function(a, b, c):
#     print(a, b, c)
#
# my_function(1, 2, 3)
#
#
# Nota: a passagem de parâmetros posicionais é intuitivamente utilizada pelas pessoas em muitas ocasiões sociais. Por exemplo, pode ser geralmente aceite que quando nos apresentamos mencionemos o(s) nosso(s) # nome(s) próprio(s) antes do nosso apelido, por exemplo, "O meu nome é Miguel Matos".
#
# A propósito, os húngaros fazem-no pela ordem inversa.
#
# Vamos implementar esse costume social em Python. A seguinte função será responsável pela introdução de alguém:
#
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")


# Consegue adivinhar o output? Execute o código e descubra se estava certo.
#
#
# Agora imagine que a mesma função está a ser utilizada na Hungria. Nesse caso, o código ficaria assim:
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")


# O output terá um aspeto diferente. Consegue adivinhá-lo?