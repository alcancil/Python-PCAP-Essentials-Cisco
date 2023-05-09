# Efeitos e resultados: listas e funções - continuação
# A segunda questão é: pode uma lista ser um resultado de uma função?
#
# Sim, claro! Qualquer entidade reconhecível por Python pode ser um resultado de uma função.
#
# Veja o código no editor. O output do programa será assim:
#
# [4, 3, 2, 1, 0]
# output
#
#
# Agora pode escrever funções com e sem resultados.
#
# Vamos mergulhar um pouco mais fundo nas questões ligadas às variáveis das funções. Isto é essencial para a criação de funções eficazes e seguras.

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))
