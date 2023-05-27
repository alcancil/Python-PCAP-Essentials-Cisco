# Mais sobre compreensões de lista
# 
# Deverá ser capaz de se lembrar das regras que regem a criação e utilização de um fenómeno Python muito especial denominado compreensão de listas - uma forma simples e muito impressionante de criar listas e # o seu conteúdo.
#
# Caso precise, fornecemos um lembrete rápido no editor.
#
# Há duas partes dentro do código, ambas criando uma lista contendo algumas das primeiras potências naturais de dez.
#
# A primeira utiliza uma forma rotineira de utilizar o loop for , enquanto a última faz uso da compreensão de lista e constrói a lista in situ, sem precisar de um loop, ou de qualquer outro código alargado.
#
# Parece que a lista é criada dentro de si mesma - não é verdade, claro, pois o Python tem de realizar quase as mesmas operações que no primeiro snippet, mas é indiscutível que o segundo formalismo é 
# simplesmente mais elegante, e permite ao leitor evitar quaisquer detalhes desnecessários.
#
# O exemplo produz duas linhas idênticas contendo o seguinte texto:
# [1, 10, 100, 1000, 10000, 100000]
# [1, 10, 100, 1000, 10000, 100000]
#
# output
#
# Execute o código para verificar se estamos certos.

list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

list_2 = [10 ** ex for ex in range(6)]

print(list_1)
print(list_2)
