# Os loops monthdays2calendar() .
#
# A classe Calendar tem vários outros métodos úteis, sobre os quais pode aprender mais na documentação (https://docs.python.org/3/library/calendar.html).
#
# Um deles é o método monthdays2calendar , que toma o ano e o mês, e, em seguida, devolve uma lista de semanas num mês específico. Cada semana é um tuple composto por números do dia e números do dia da 
# semana. Veja o código no editor.
#
# Note-se que os números dos dias fora do mês são representados por 0, enquanto os números do dia da semana são um número de 0-6, onde 0 é segunda-feira e 6 é domingo.
#
# Dentro de momentos, este método pode ser-lhe útil para completar uma tarefa de laboratório. Está preparado?

import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)
