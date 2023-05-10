# Funções selecionadas a partir do módulo random : continuação
#
# As funções randrange e randint .
# 
# Se quiser valores inteiros aleatórios, uma das seguintes funções encaixar-se-ia melhor:
#
#    randrange(end)
#    randrange(beg, end)
#    randrange(beg, end, step)
#    randint(left, right)
#
# As três primeiras invocações gerarão um número inteiro retirado (pseudo aleatoriamente) do intervalo (respetivamente):
#
#    range(end)
#    range(beg, end)
#    range(beg, end, step)
#
# Note-se a exclusão implícita do lado direito!
#
# A última função é um equivalente a randrange(left, right+1) - gera o valor inteiro i, que cai no intervalo [esquerda, direita] (sem exclusão do lado direito).
#
# Veja o código no editor. Este programa de amostra produzirá consequentemente uma linha composta por três zeros e um zero ou um no quarto lugar.


from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))