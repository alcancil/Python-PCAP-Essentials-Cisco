# Passagem de argumentos de keyword
# O Python oferece outra convenção para passar argumentos, onde o significado do argumento é ditado pelo seu nome, não pela sua posição - chama-se keyword argument passing.
#
# Veja o snippet:
#
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


# O conceito é claro - os valores passados para os parâmetros são precedidos pelos nomes dos parâmetros alvo, seguidos do sinal = .
#
# A posição não importa aqui - o valor de cada argumento conhece o seu destino com base no nome utilizado.
#
# Deverá ser capaz de prever o output. Execute o código para verificar se estava certo.
#
# É claro que não se deve usar um nome de parâmetro inexistente.
#
# O snippet seguinte causará um erro de runtime:
#
# def introduction(first_name, last_name):
#     print("Hello, my name is", first_name, last_name)
#
# introduction(surname="Skywalker", first_name="Luke")
#
#
# Isto é o que Python lhe dirá:
#
# TypeError: introduction() got an unexpected keyword argument 'surname'
# output


# Experimente você mesmo.