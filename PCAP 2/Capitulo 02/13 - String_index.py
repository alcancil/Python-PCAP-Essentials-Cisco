# Operações em strings: o método index() .
#
# A classe index() (é um método, não uma função) pesquisa a sequência desde o início, a fim de encontrar o primeiro elemento do valor especificado no seu argumento.
#
# Nota: o elemento pesquisado deve ocorrer na sequência - a sua ausência causará uma exceção ValueError .
#
# O método devolve o index da primeira ocorrência do argumento (o que significa que o menor resultado possível é 0, enquanto o maior é o comprimento do argumento decrescido por 1). 


# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))