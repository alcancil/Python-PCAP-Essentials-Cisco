# A declaração elif .
# O segundo caso especial introduz outra nova keyword de Python: elif. Como provavelmente suspeitará, é uma forma mais curta de else if.
#
# elif é usado para verificar mais do que uma condição, e para parar quando a primeira afirmação que é verdadeira é encontrada.
#
# O nosso próximo exemplo assemelha-se a nesting, mas as semelhanças são muito ligeiras. Mais uma vez, vamos mudar os nossos planos e expressá-los como # se segue: Se o tempo estiver bom, iremos dar um passeio, caso contrário, se conseguirmos bilhetes, iremos ao teatro, caso contrário, se houver mesas # livres no restaurante, iremos almoçar; se tudo o resto falhar, regressaremos a casa e jogaremos xadrez.
#
# Já reparou quantas vezes utilizámos as palavras caso contrário? Esta é a fase em que a keyword elif desempenha o seu papel.
# 
# Vamos escrever o mesmo cenário usando Python:
#
# if the_weather_is_good:
#    go_for_a_walk()
# elif tickets_are_available:
#    go_to_the_theater()
# elif table_is_available:
#    go_for_lunch()
# else:
#     play_chess_at_home()
#
#
# A forma de reunir as declarações subsequentes if-elif-else é por vezes chamada de cascade (cascata).
#
# Repare novamente como a indentação melhora a legibilidade do código.
#
# Neste caso, deve ser dada alguma atenção adicional:
#
# não deve usar else sem um precedente if;
# else é sempre o último ramo da cascade, independentemente de ter utilizado elif ou não;
# else é uma parte opcional da cascade, e pode ser omitida;
# se houver um else ramo na cascade, apenas um de todos os ramos é executado;
# se não houver nenhum else ramo, é possível que nenhuma das ramificações disponíveis seja executada.
#
# Isto pode parecer um pouco confuso, mas esperemos que alguns exemplos simples ajudem a lançar mais luz.