# Adicionar elementos a uma lista: continuação
# Pode iniciar a vida de uma lista tornando-a vazia (isto é feito com um par de parêntesis retos vazio) e 
# depois adicionando-lhe novos elementos conforme necessário.
#
# Veja o snippet no editor. Tente adivinhar o seu output após a execução do loop for . Execute o programa 
# para verificar se estava certo.
#
# Será uma sequência de números inteiros consecutivos a partir de 1 (depois adiciona-se um a todos os 
# valores anexados) até 5.
#
#
# Modificámos um pouco o snippet:
#
# my_list = []  # Creating an empty list.
#
# for i in range(5):
#    my_list.insert(0, i + 1)
#
# print(my_list)
#
#
# O que acontecerá agora? Execute o programa e verifique se desta vez também estava certo.
#
#
# Deve obter a mesma sequência, mas em ordem inversa (este é o mérito de usar o método insert() ).

my_list = [] # cria uma lista vazia

for i in range(5) :
    my_list.append(i + 1)

print(my_list)