# Aceder ao conteúdo da lista
# Cada um dos elementos da lista pode ser acedido separadamente. Por exemplo, pode ser impresso:
#
# print(numbers[0]) # Accessing the list's first element.
#
#
# Assumindo que todas as operações anteriores tenham sido concluídas com sucesso, o snippet enviará 111 para a consola.
#
# Como pode ver no editor, a lista também pode ser impressa como um todo - tal como aqui:
#
# print(numbers)  # Printing the whole list.
#
#
# Como provavelmente já notou antes, o Python decora o output de uma forma que sugere que todos os valores apresentados formam uma lista. O output do 
# exemplo acima é o seguinte:
#
# [111, 1, 7, 2, 1]
# output
#
#
# O método len() .
# O comprimento de uma lista pode variar durante a execução. Novos elementos podem ser acrescentados à lista, enquanto outros podem ser retirados da 
# mesma. Isto significa que a lista é uma entidade muito dinâmica.
#
# Se quiser verificar o comprimento atual da lista, pode usar uma função chamada len() (o seu nome vem de length (comprimento)).
#
# A função toma o nome da lista como argumento, e devolve o número de elementos atualmente armazenados dentro da lista (por outras palavras - o 
# comprimento da lista).
#
# Veja a última linha de código no editor, execute o programa e verifique que valor irá imprimir para a consola. Consegue adivinhar?


numbers = [10, 5, 7, 2, 1]
print("A lista original é : ", numbers)

numbers[0] = 111
print("\n Nova lista : ", numbers)

numbers[1] = numbers[4]
print("\n Nova lista : ", numbers)

print("\n Tamanho da lista: ", len(numbers)) 