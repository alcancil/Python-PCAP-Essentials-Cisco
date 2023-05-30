# Criação de um objecto de data utilizando o formato ISO
#
# O módulo datetime fornece vários métodos para criar um objeto date . Um deles é o método fromisoformat , que tem uma data no formato YYYY-MM-DD em conformidade com a norma ISO 8601.
#
# A norma ISO 8601 define a forma como a data e a hora são representadas. É muitas vezes utilizada, pelo que vale a pena tomar um momento para se familiarizar com ela. Veja a imagem descrevendo os valores 
# exigidos pelo formato:
#
# yyy - year ( e.g 1980 )
# MM - Month ( e.g, 11 )
# DD - Day ( e.g, 18 )
#
#
# 
# O formato de data e hora ISO 8601
#
# 
# Agora olhe para o código no editor e execute-o.
#
# No nosso exemplo, YYYY é 2019, MM é 11 (novembro) e DD é 04 (quarto dia de novembro).
#
# Ao substituir a data, certifique-se de acrescentar 0 antes de um mês ou de um dia que seja expresso por um número inferior a 10.
#
# Note: O método fromisoformat está disponível em Python desde a versão 3.7.

# Em formato americano (YYY-MM-DD)
from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)
print()

# Formato Brasileiro(DD/MM/AAAA)

from datetime import date

d = date.fromisoformat('2019-11-04')
date_formatado = d.strftime("%d/%m/%Y")
print(date_formatado)