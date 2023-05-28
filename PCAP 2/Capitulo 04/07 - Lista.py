# Mais sobre as compreensões de lista: continuação
#
# Há uma sintaxe muito interessante que queremos mostrar-lhe agora. A sua usabilidade não se limita a compreensões de lista, mas temos de admitir que as compreensões são o ambiente ideal para ela.
#
# É uma expressão condicional - uma forma de selecionar um de dois valores diferentes com base no resultado de uma expressão Booleana.
#
# Veja:
#
# expression_one if condition else expression_two
#
# Pode parecer um pouco surpreendente à primeira vista, mas é preciso ter em mente que não se trata de uma instrução condicional. Além disso, não é uma instrução de todo. É um operador.
#
# O valor que ele fornece é igual a expression_one quando a condição é True, e expression_two caso contrário.
#
# Um bom exemplo dir-lhe-á mais. Veja o código no editor.
#
# O código preenche uma lista com 1e 0- se o index de um determinado elemento for estranho, o elemento é definido para 0, e para 1 caso contrário.
#
# Simples? Talvez não à primeira vista. Elegante? Indiscutivelmente.
#
# Pode-se usar o mesmo truque dentro de uma compreensão de lista? Sim, pode-se.

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)