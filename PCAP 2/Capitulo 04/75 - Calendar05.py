# Os loops weekday() .
#
# Outra função útil fornecida pelo módulo calendar é a função chamada weekday, que devolve o dia da semana como um valor inteiro para o ano, mês e dia em questão. Vamos vê-la na prática.
#
# Execute o código no editor para verificar o dia da semana que cai a 24 de dezembro de 2020.
# 
# Resultado:
# 3
#
# output
#
# A função weekday devolve 3, o que significa que 24 de dezembro de 2020 é uma quinta-feira.


import calendar
print(calendar.weekday(2020, 12, 24))
