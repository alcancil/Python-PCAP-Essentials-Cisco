# Criar objetos timedelta .
#
# Já aprendeu que um objeto timedelta pode ser devolvido como o resultado de subtrair dois objetos date ou datetime .
#
# É claro que também pode criar um objeto por si próprio. Para este efeito, vamos conhecer os argumentos aceites pelo construtor da classe, que são: days, seconds, microseconds, milliseconds, minutes, hours, # e weeks. Cada um deles é opcional e o padrão é 0.
#
# Os argumentos devem ser números inteiros ou floating point, e podem ser positivos ou negativos. Vejamos um exemplo simples no editor.

from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)


# Resultado:
# 16 days, 3:00:00
#
# output
#
# O resultado de 16 dias é obtido através da conversão do argumento weeks para dias (2 semanas = 14 dias) e adicionando o argumento days (2 dias). Este é um comportamento normal, porque o objeto timedelta 
# armazena internamente apenas dias, segundos e microssegundos. Da mesma forma, o argumento hour é convertido em minutos. Veja o exemplo abaixo:
#
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

# Resultado:
# Days: 16
# Seconds: 10800
# Microseconds: 0
# 
# output
# 
# O resultado de 10800 é obtido convertendo 3 horas em segundos. Desta forma, o objeto timedelta armazena os argumentos passados durante a sua criação. As semanas são convertidas em dias, horas e minutos em 
# segundos, e milissegundos em microssegundos.
