# Operações em strings: min()
#
# Agora que compreende que as strings são sequências, podemos mostrar-lhe algumas capacidades de sequência menos óbvias. Vamos apresentá-las utilizando strings, mas não se esqueça de que as listas também 
# podem adotar os mesmos truques.
#
# Vamos começar com uma função chamada min().
#
# A função encontra o elemento mínimo da sequência passada como um argumento. Há uma condição - a sequência (string, lista, não importa) não pode estar vazia, ou então terá uma exceção ValueError .
#
# O programa do Exemplo 1 tem como output:
# A
#
# output
#
# Nota: É uma maiúscula A. Porquê? Lembre-se da tabela ASCII - que letras ocupam os primeiros locais - superior ou inferior?
#
# Preparámos mais dois exemplos para analisar: Exemplos 2 & 3.
#
# Como pode ver, eles apresentam mais do que apenas strings. O output esperado parece-se com o seguinte:
# [ ]
# 0
#
# output
#
# Nota: usamos os parêntesis retos para evitar que o espaço seja negligenciado no ecrã.

# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 &amp; 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))