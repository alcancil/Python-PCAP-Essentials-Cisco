# Como verificamos se um ano é um ano bissexto?
#
# O módulo calendar fornece duas funções úteis para verificar se os anos são anos bissextos.
#
# 29 de fevereiro
#
#
# O primeiro, chamado isleap, devolve True se o ano passado for bissexto, ou False caso contrário. O segundo, chamado leapdays, devolve o número de anos bissextos num determinado intervalo de anos.
#
# Execute o código no editor.
#
# Resultado:
# True
# 3
#
# output
#
# No exemplo, obtemos o resultado 3, porque no período de 2010 a 2020 há apenas três anos bissextos (nota: 2021 não está incluído). São os anos de 2012, 2016 e 2020.

import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.
