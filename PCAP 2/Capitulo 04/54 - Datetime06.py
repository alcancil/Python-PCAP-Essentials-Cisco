# Que dia da semana é hoje?
#
# Um dos métodos mais úteis que facilita o trabalho com datas é o método chamado weekday. Ele devolve o dia da semana como um número inteiro, onde 0 é segunda-feira e 6 é domingo. Execute o código no editor.
#

from datetime import date

d = date(2019, 11, 4)
print(d.weekday())

# Resultado:
# 0
#
# output
#
# Um homem e o calendário - que dia é hoje?
#
#
# A classe date tem um método semelhante chamado isoweekday, que também devolve o dia da semana como um inteiro, mas 1 é segunda-feira, e 7 é domingo:

from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())

# Resultado:
# 1
#
# output
#
# Como pode ver, para a mesma data recebemos um número inteiro diferente, mas expressando o mesmo dia da semana. O número inteiro devolvido pelo método isodayweek segue a especificação ISO 85601.
