# Os loops gmtime() e localtime() .
#
# Algumas das funções disponíveis no módulo time requerem conhecimento da classe struct_time, mas antes de os conhecermos, vamos ver como é a classe:
#
# time.struct_time:
#    tm_year   # specifies the year
#    tm_mon    # specifies the month (value from 1 to 12)
#    tm_mday   # specifies the day of the month (value from 1 to 31)
#    tm_hour   # specifies the hour (value from 0 to 23)
#    tm_min    # specifies the minute (value from 0 to 59)
#    tm_sec    # specifies the second (value from 0 to 61 )
#    tm_wday   # specifies the weekday (value from 0 to 6)
#    tm_yday   # specifies the year day (value from 1 to 366)
#    tm_isdst  # specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
#    tm_zone   # specifies the timezone name (value in an abbreviated form)
#    tm_gmtoff # specifies the offset east of UTC (value in seconds)
#
# A classe struct_time também permite o acesso a valores utilizando indexes. Index 0 devolve o valor em tm_year, enquanto 8 devolve o valor em tm_isdst.
#
# As exceções são tm_zone e tm_gmoff, que não podem ser acedidas utilizando indexes. Vejamos como utilizar na prática a classe struct_time. Execute o código no editor.
#
# Resultado:
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
#
# output
#
# O exemplo mostra duas funções que convertem o tempo decorrido da época Unix para o objeto struct_time. A diferença entre eles é que a função gmtime devolve o objeto struct_time em UTC, enquanto a função 
# localtime devolve a hora local. Para a função gmtime , o atributo tm_isdst é sempre 0.

import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
