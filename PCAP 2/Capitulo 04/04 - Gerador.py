
# A função yield .
# 
# O protocolo iterador não é particularmente difícil de compreender e utilizar, mas também é indiscutível que o protocolo é bastante inconveniente.
# 
# O principal desconforto que traz é a necessidade de guardar o estado da iteração entre subsequentes invocações __iter__ .
#
# Por exemplo, o iterador Fib é forçado a armazenar com precisão o local onde a última invocação foi interrompida (ou seja, o número avaliado e os valores dos dois elementos anteriores). Isso torna o código # maior e menos compreensível.
# 
# É por isso que o Python oferece uma maneira muito mais eficaz, conveniente e elegante de escrever iteradores.
# 
# O conceito é fundamentalmente baseado num mecanismo muito específico e poderoso fornecido pela keyword yield .
# 
# Pode pensar na keyword yield como uma irmã mais inteligente da declaração return , com uma diferença essencial.
# 
# Dê uma vista de olhos nesta função:
# def fun(n):
#     for i in range(n):
#         return i
#
#
# Tem um aspecto estranho, não tem? É claro que o loop for não tem qualquer hipótese de terminar a sua primeira execução, uma vez que o return vai quebrá-lo irrevogavelmente.
#
# Além disso, invocar a função não mudará nada - o loop for começará do zero e será quebrado imediatamente.
# 
# Podemos dizer que tal função não é capaz de guardar e restaurar o seu estado entre invocações subsequentes.
#
# Isto também significa que uma função como esta não pode ser usada como gerador.
#
#
#
# Substituímos exatamente uma palavra no código - consegue vê-la?
# def fun(n):
#    for i in range(n):
#        yield i
#
#
# Adicionámos yield em vez de return. Esta pequena emenda transforma a função num gerador, e executar a declaração yield tem alguns efeitos muito interessantes.
#
# Antes de mais, fornece o valor da expressão especificada após a keyword yield , assim como return, mas não perde o estado da função.
#
# Todos os valores das variáveis são congelados e aguardam a próxima invocação, quando a execução é retomada (não tirada do zero, como depois return).
#
# Há uma limitação importante: tal função não deve ser invocada explicitamente porque - na realidade - já não é uma função; é um objeto gerador.
#
# A invocação devolverá o identificador do objeto, não a série que esperamos do gerador.
#
# Devido às mesmas razões, a função anterior (a função com a declaração return ) só pode ser invocada explicitamente, e não deve ser usada como um gerador.
# Como construir um gerador
#
# Deixe-nos mostrar-lhe o novo gerador em ação.
#
# É assim que podemos utilizá-lo:

def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

