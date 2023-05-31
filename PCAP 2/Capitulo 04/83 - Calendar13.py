# Cenário
#
# Durante este curso, olhámos um pouco para a classe Calendar . A sua tarefa é alargar a sua funcionalidade com um novo método chamado count_weekday_in_year, que toma como parâmetros um ano e um dia da semana # e, em seguida, devolve o número de ocorrências de um dia da semana específico no ano.
#
# Use as seguintes dicas:
#
#    Crie uma classe chamada MyCalendar que estende a classe Calendar ;
#    crie o método count_weekday_in_year com os parâmetros do ano e do dia da semana. O parâmetro do dia da semana deve ser um valor entre 0-6, onde 0 é segunda-feira e 6 é domingo. O método deve devolver o 
# número de dias como um inteiro;
#    na sua implementação, use o método monthdays2calendar da classe Calendar .
#
# Os resultados esperados são os seguintes:
#
# Argumentos de amostra
#
# year=2019, weekday=0

from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day in week:
                    if day[0] != 0 and day[1] == weekday:
                        count += 1
        return count

# Exemplo de uso
my_calendar = MyCalendar()
result = my_calendar.count_weekday_in_year(2019, 0)
print(result)