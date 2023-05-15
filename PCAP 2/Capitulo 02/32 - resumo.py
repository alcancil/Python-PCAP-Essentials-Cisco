
# Key takeaways
#
# 1. Alguns dos métodos oferecidos por strings são:
#
#    capitalize() — alterar todas as letras da string para maiúsculas;
#    center() — centrar a string dentro do campo de um comprimento conhecido;
#    count() — contar as ocorrências de um determinado caratere;
#    join() — juntar todos os itens de uma tuple/lista numa string;
#    lower() — converter todas as letras da string em letras minúsculas;
#    lstrip() — remover os carateres brancos desde o início da string;
#    replace() — substituir uma determinada substring por outra;
#    rfind() — encontrar uma substring a partir do final da string;
#    rstrip() — remover os espaços em branco à direita do final da string;
#    split() — dividir a string numa substring usando um determinado delimitador;
#    strip() — remover os espaços em branco à esquerda e à direita;
#    swapcase() — trocar letras maiúsculas e minúsculas (minúsculas para maiúsculas e vice-versa)
#    title() — tornar a primeira letra de cada palavra uma maiúscula;
#    upper() — converter todas as letras da string em letras maiúsculas.
#
#
# 2. O conteúdo das strings pode ser determinado utilizando os seguintes métodos (todos eles devolvem valores Booleanos):
#
#    endswith() — a string termina com uma determinada substring?
#    isalnum() — a string consiste apenas em letras e dígitos?
#    isalpha() — a string consiste apenas em letras?
#    islower() — a string consiste apenas em letras minúsculas?
#    isspace() — a string consiste apenas em espaços em branco?
#    isupper() — a string consiste apenas em letras maiúsculas?
#    startswith() — a string começa com uma determinada substring?
#
#
# Exercício 1
#
# Qual é o output esperado do seguinte código?
for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
#
#
# ABC123xyz
#
#
# Exercício 2
#
# Qual é o output esperado do seguinte código?
s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])

#
# of
#
#
# Exercício 3
#
# Qual é o output esperado do seguinte código?
the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)

#
# Where*are*the*snows?
#
#
# Exercício 4
#
# Qual é o output esperado do seguinte código?
s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)


# It is either hard or possible
