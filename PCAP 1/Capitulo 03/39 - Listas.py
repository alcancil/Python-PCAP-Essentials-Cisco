# LISTAS
#
#
# Imagine que se queira perguntar ao usuário: Digite 1.000 ítens e depois imprima um a um esses mil itens. Terimaos que executar 1.000 vezes a funcao 
# print ?
#
# Para esses casos fora inventados as listas
#
# Elas seguem a sintaxe:
# 
# lista = [1, 2, 3, 4, 5, ...., 1000]
#
# Com isso as repostas são colocadas dentro dessa lista e só é necessário se imprimir a lista para se obter todos os 1.000 itens da lista
#
# Indexar listas
# Como se altera o valor de um elemento escolhido na lista?
#
# Vamos atribuir um novo valor de 111 ao primeiro elemento na lista. Fazemo-lo assim:
#
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.
#
numbers[0] = 111
print("New list content: ", numbers)  # Current list content.
#
#
# E agora queremos que o valor do quinto elemento seja copiado para o segundo elemento - consegue adivinhar como o fazer?
#
numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\n Previous list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("\n New list content:", numbers)  # Printing current list content.
#
#
# O valor dentro dos parêntesis que seleciona um elemento da lista é chamado um index, enquanto a operação de selecionar um elemento da lista é 
# conhecida como indexing (indexação).
#
# Vamos utilizar a função print() para imprimir o conteúdo da lista cada vez que fazemos as alterações. Isto ajudar-nos-á a seguir cada passo com mais # cuidado e a ver o que se passa após uma determinada modificação da lista.
#
# Nota: todos os índices usados até agora são literais. Os seus valores são fixados em runtime, mas qualquer expressão também pode ser o index. Isto 
# oferece muitas possibilidades.
#