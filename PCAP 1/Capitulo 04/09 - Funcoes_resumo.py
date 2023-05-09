# Key takeaways
# 1. É possível passar informações para funções utilizando parâmetros. As suas funções podem ter todos os parâmetros que precisar.
#
# Um exemplo de uma função de um parâmetro:
#
def hi(name):
    print("Hi,", name)

hi("Greg")
#
#
# Um exemplo de uma função de dois parâmetros:

def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")


# Um exemplo de uma função de três parâmetros:

def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)


# 2. Pode passar argumentos a uma função utilizando as seguintes técnicas:
#
# passagem de argumento posicional onde a ordem de passagem dos argumentos importa (Ex. 1),
# passagem de argumento de keyword (nomeada) onde a ordem dos argumentos passados não importa (Ex. 2),
# uma mistura de passagem de argumentos posicionais e de keyword (Ex. 3).
# Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3


# É importante lembrar que os argumentos posicionais não devem seguir os argumentos de keyword. É por isso que se tentar executar o seguinte snippet:
#
# def subtra(a, b):
#    print(a - b)
#
# subtra(5, b=2)    # outputs: 3
# subtra(a=5, 2)    # Syntax Error
#
# O Python não o deixará fazê-lo através da sinalização de um SyntaxError.
#
#
#
#
# 3. Pode usar a técnica de passagem de argumentos de keyword para pré-definir um valor para um determinado argumento:
#
def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")




# Exercício 1
#
# Qual é o output do seguinte snippet?

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()


# Verifique
# My name is Bond. James Bond.
#
# Exercício 2
#
# Qual é o output do seguinte snippet?

def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")


# Verifique
# My name is Sean Connery. James Bond.
#
# Exercício 3
#
# Qual é o output do seguinte snippet?

def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")


# Verifique
# My name is Bond. Susan.
#
# Exercício 4
#
# Qual é o output do seguinte snippet?
#
# def add_numbers(a, b=2, c):
#     print(a + b + c)
#
# add_numbers(a=1, c=3)
#
#
# Verifique
# SyntaxError - um argumento não padrão (c) segue um argumento padrão (b=2)