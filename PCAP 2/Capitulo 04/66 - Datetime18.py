# Operações de data e hora
#
# Mais cedo ou mais tarde, terá de efetuar alguns cálculos sobre a data e hora. Felizmente, há uma classe chamada timedelta no módulo datetime que foi criado precisamente para esse fim.
#
# Para criar um objeto timedelta , basta fazer a subtração nos objetos date ou datetime , assim como fizemos no exemplo no editor. Execute-o.
#
# Resultado:
# 366 days, 0:00:00
# 365 days, 9:07:00
#
# output
#
# O exemplo mostra a subtração para ambos os objetos date e datetime . No primeiro caso, recebemos a diferença em dias, que é de 366 dias. Observe que a diferença em horas, minutos e segundos também é 
# exibida. No segundo caso, recebemos um resultado diferente, porque especificámos o tempo que foi incluído nos cálculos. Como resultado, recebemos 365 dias, 9 horas e 7 minutos.
#
# Daqui a pouco irá aprender mais sobre a criação de objetos timedelta e sobre as operações que pode fazer com eles.

from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
