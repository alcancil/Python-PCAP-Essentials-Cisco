# Lambdas e a função filter() .
#
# Outra função Python que pode ser significativamente embelezada pela aplicação de um lambda é filter().
#
# Espera o mesmo tipo de argumentos que map(), mas faz algo diferente - filtra o seu segundo argumento ao mesmo tempo que é guiado por instruções que fluem da função especificada como o primeiro argumento (a # função é invocada para cada elemento da lista, tal como em map()).
#
# Os elementos que retornam True da função passam o filtro - os outros são rejeitados.
#
# O exemplo no editor mostra a função filter() em ação.
#
# Nota: fizemos uso do módulo random para inicializar o gerador de números aleatórios (não confundir com os geradores de que acabámos de falar) com a função seed() , e para produzir cinco valores inteiros 
# aleatórios a partir de -10 até 10 utilizando a função randint() .
#
# A lista é então filtrada, e apenas os números que são iguais e superiores a zero são aceites.
#
# Claro que não é provável que receba os mesmos resultados, mas os nossos resultados são estes:
# [6, 3, 3, 2, -7]
# [6, 2]

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)