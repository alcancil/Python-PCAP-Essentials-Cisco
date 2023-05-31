# Os loops itermonthdates() .
#
# A classe Calendar tem vários métodos que devolvem um iterador. Um deles é o método itermonthdates , que requer a especificação do ano e mês.
#
# Como resultado, todos os dias no mês e ano especificados são devolvidos, tal como todos os dias antes do início do mês ou do final do mês que são necessários para obter uma semana completa.
#
# Cada dia é representado por um objeto datetime.date . Dê uma vista de olhos no exemplo no editor.
#
# O código exibe todos os dias de novembro de 2019. Como o primeiro dia de novembro de 2019 foi uma sexta-feira, os dias seguintes também são devolvidos para obter a semana completa: 10/28/2019 (segunda-
# feira) 10/29/2019 (terça-feira) 10/30/2019 (quarta-feira) 10/31/2019 (quinta-feira).
#
# O último dia de novembro de 2019 foi um sábado, portanto, para manter a semana completa, mais um dia é devolvido 12/01/2019 (sexta-feira).


import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
