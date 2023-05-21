# A stack - a abordagem processual
#
# Primeiro, é preciso decidir como armazenar os valores que chegarão à stack. Sugerimos a utilização do mais simples dos métodos, e o emprego de uma lista para este trabalho. Vamos assumir que o tamanho da 
# stack não é limitado de forma alguma. Vamos também assumir que o último elemento da lista armazena o elemento superior.
#
# A stack em si já está criada:
# stack = []
#
#
# Estamos prontos para definir uma função que coloca um valor na stack. Aqui estão os pressupostos para tal:
#
#    o nome para a função é push;
#    a função obtém um parâmetro (este é o valor a ser colocado na stack)
#    a função não devolve nada;
#    a função anexa o valor do parâmetro ao fim da stack;
#
# Foi assim que o fizemos - dê uma vista de olhos:
# def push(val):
#     stack.append(val)
#
#
# Agora é tempo de uma função tirar um valor da stack. É assim que o pode fazer:
#
#    o nome da função é pop;
#    a função não obtém nenhum parâmetro;
#    a função devolve o valor retirado da stack
#    a função lê o valor da parte superior da stack e remove-o.
#
# A função está aqui:
# def pop():
#     val = stack[-1]
#     del stack[-1]
#    return val
#
#
# Nota: a função não verifica se existe algum elemento na stack.
#
# Vamos juntar todas as peças para pôr a stack em movimento. O programa completo empurra três números para a stack, puxa-os para fora e imprime os seus valores no ecrã. Pode vê-lo na janela do editor.
#
# O programa faz output do seguinte texto para o ecrã:
# 1
# 2
# 3

stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
