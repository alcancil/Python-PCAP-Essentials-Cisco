# Os loops in e not in operadores
# O Python oferece dois operadores muito poderosos, capazes de olhar através da lista a fim de verificar se um valor específico está ou não armazenado dentro da lista
#
# Estes operadores são:
#
# elem in my_list
# elem not in my_list
#
#
# O primeiro deles (in) verifica se um dado elemento (o seu argumento da esquerda) está atualmente armazenado algures dentro da lista (o argumento da direita) - o operador devolve True neste caso.
#
# O segundo (not in) verifica se um dado elemento (o seu argumento da esquerda) está ausente numa lista - o operador devolve True neste caso.
# 
# Veja o código no editor. O snippet mostra ambos os operadores em ação. Consegue adivinhar o seu output? Execute o programa para verificar se estava certo.

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)
