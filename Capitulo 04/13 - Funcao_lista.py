# Efeitos e resultados: listas e funções
# Há duas questões adicionais que devem ser respondidas aqui.
#
# A primeira é: pode uma lista ser enviada para uma função como argumento?
#
# Claro que pode! Qualquer entidade reconhecível pelo Python pode desempenhar o papel de um argumento de função, embora tenha de ter a certeza de que a função é capaz de lidar com ela.
#
# Assim, se passar uma lista a uma função, a função tem de lidar com ela como uma lista.
#
# Uma função como esta aqui:
#
# def list_sum(lst):
#    s = 0
#    
#    for elem in lst:
#        s += elem
#    
#    return s
#
#
# e invocada assim:
#
# print(list_sum([5, 4, 3]))
#
#
# irá devolver 12 como resultado, mas deve esperar problemas se a invocar desta forma arriscada:
#
# print(list_sum(5))
#
#
# A resposta do Python será inequívoca:
#
# TypeError: 'int' object is not iterable
# output
#
#
# Isto é causado pelo facto de que um único valor inteiro não deve ser iterado pelo loop for .

def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5]))
print(list_sum([5, 4, 3]))
print(list_sum([10, 20, 30, 40, 50, 60]))

