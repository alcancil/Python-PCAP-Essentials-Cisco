# Criar objetos timedelta : continuação
#
# Já sabe como o objeto timedelta armazena os argumentos passados internamente. É tempo de ver como pode ser utilizado na prática.
#
# Vejamos algumas operações apoiadas pelas classes do módulo datetime . Execute o código que fornecemos no editor.

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)


# Resultado:
# 16 days, 2:00:00
# 32 days, 4:00:00
# 2019-11-05
# 2019-11-05 18:53:00
#
# output
#
# A função timedelta pode ser multiplicado por um inteiro. No nosso exemplo, multiplicamos o objeto que representa 16 dias e 2 horas por 2. Como resultado, recebemos um objeto timedelta representando 32 dias # e 4 horas.
#
# Note que tanto os dias como as horas foram multiplicados por 2. Outra operação interessante usando o objeto timedelta é a adição. No exemplo, adicionamos o objeto timedelta à data e datetime objetos.
#
# Como resultado destas operações, recebemos data e objetos datetime aumentados em dias e horas armazenados no timedelta objeto.
#
# A operação de multiplicação apresentada permite-lhe aumentar rapidamente o valor do objeto timedelta , enquanto a multiplicação pode também ajudá-lo a obter uma data no futuro.
#
# Claro, as classes timedelta, date, e datetime suportam muitas mais operações. Encorajamo-lo a familiarizar-se com elas na documentação.