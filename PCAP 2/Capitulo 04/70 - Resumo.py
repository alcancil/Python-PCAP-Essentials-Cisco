
# Key takeaways
#
# 1. Para criar um objeto date , deve passar os argumentos do ano, mês e dia como se segue:
#

from datetime import date

my_date = date(2020, 9, 29)
print("Year:", my_date.year) # Year: 2020
print("Month:", my_date.month) # Month: 9
print("Day:", my_date.day) # Day: 29
print()

# O objeto date tem três atributos (somente de leitura): ano, mês e dia.
#
# 2. O método today devolve um objeto de data que representa a data local atual:

from datetime import date
print("Today:", date.today()) # Displays: Today: 2020-09-29
print()


# 3. Em Unix, o timestamp expressa o número de segundos desde 1 de janeiro de 1970, 00:00:00 (UTC). Esta data é chamada "época Unix", porque começou a contagem do tempo nos sistemas Unix. O timestamp é na 
# realidade a diferença entre uma determinada data (incluindo a hora) e 1 de janeiro de 1970, 00:00:00 (UTC), expressa em segundos. Para criar um objeto de data a partir de um timestamp, temos de passar um # timestamp Unix para o método fromtimestamp :

from datetime import date
import time

timestamp = time.time()
d = date.fromtimestamp(timestamp)
print(d)
print()

# Note: A função time devolve o número de segundos desde 1 de janeiro de 1970 até ao momento atual sob a forma de um número float.
#
# 4. O construtor da classe time aceita seis argumentos (hora, minuto, segundo, microssegundo, tzinfoe fold). Cada um destes argumentos é opcional.

from datetime import time

t = time(13, 22, 20)

print("Hour:", t.hour) # Hour: 13
print("Minute:", t.minute) # Minute: 22
print("Second:", t.second) # Second: 20


# 5. O módulo time contém a função sleep , que suspende a execução do programa por um determinado número de segundos, por exemplo:
# 

import time

time.sleep(10)
print("Hello world!") # This text will be displayed after 10 seconds.


# 6. no módulo datetime , data e hora podem ser representados como objetos separados ou como um único objeto. A classe que combina data e hora é chamada datetime. Todos os argumentos passados ao construtor # vão para atributos de classe só de leitura. São ano, mês, dia, hora, minuto, segundo, microssegundo, tzinfoe fold:

from datetime import datetime

dt = datetime(2020, 9, 29, 13, 51)
print("Datetime:", dt) # Displays: Datetime: 2020-09-29 13:51:00


# 7. O método strftime só aceita um argumento sob a forma de uma string especificando um formato que pode consistir em diretivas. Uma diretiva é uma string que consiste no caratere % (percentagem) e uma 
# letra minúscula ou maiúscula. Abaixo estão algumas diretivas úteis:
#
#    %Y – devolve o ano com o século como um número decimal;
#    %m — devolve o mês como um número decimal de zero;
#    %d — devolve o dia como um número decimal de zero;
#    %H — devolve a hora como um número decimal de zero;
#    %M — devolve o minuto como um número decimal de zero;
#    %S — devolve o segundo como um número decimal de zero.
#
# Exemplo:

from datetime import date

d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Displays: 2020/09/29


# 8. É possível realizar cálculos em objetos date e datetime , por exemplo:
#

from datetime import date

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

d = d1 - d2
print(d) # Displays: 366 days, 0:00:00.
print(d * 2) # Displays: 732 days, 0:00:00.
print()

# O resultado da subtração é devolvido como um objeto timedelta que expressa a diferença em dias entre as duas datas no exemplo acima.
#
# Observe que a diferença em horas, minutos e segundos também é exibida. O objeto timedelta pode ser usado para cálculos adicionais (por exemplo, pode multiplicá-lo por 2).
#
#
#
# Exercício 1
#
# Qual é o output do seguinte snippet?

from datetime import time

t = time(14, 39)
print(t.strftime("%H:%M:%S"))
print()

# 14:53:00


# Exercício 2
# 
# Qual é o output do seguinte snippet?

from datetime import datetime

dt1 = datetime(2020, 9, 29, 14, 41, 0)
dt2 = datetime(2020, 9, 28, 14, 41, 0)

print(dt1 - dt2)
print()

# 1 day, 0:00:00


