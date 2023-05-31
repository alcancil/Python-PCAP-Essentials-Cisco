# Os loops strptime() método
#
# Saber como criar um formato pode ser útil ao usar um método chamado strptime na datetime classe. Ao contrário do método strftime , este cria um objeto datetime a partir de uma string representando uma data  # hora.
#
# O método strptime requer que se especifique o formato em que se guardou a data e hora. Vejamo-lo num exemplo. Dê uma vista de olhos ao código no editor.
#
# Resultado:
# 2019-11-04 14:53:00
#
# output
#
# No exemplo, especificámos dois argumentos necessários. O primeiro é uma data e hora como uma string: "2019/11/04 14:53:00", enquanto o segundo é um formato que facilita a análise para um datetime objeto. 
# Tenha cuidado, porque se o formato especificado não corresponder à data e hora na string, levantará um ValueError.
#
# Nota: No módulo time , pode encontrar uma função chamada strptime, que analisa uma string representando um tempo para um objeto struct_time. A sua utilização é análoga à do módulo strptime na classe 
# datetime :
#
# import time
# print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
#
# O seu resultado será o seguinte:
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)


from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
print()

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
