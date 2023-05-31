# Obter um timestamp
#
# Existem muitos conversores disponíveis na Internet que podem calcular um timestamp com base numa determinada data e hora, mas como o podemos fazer no módulo datetime ?
#
# Isto é possível graças ao método timestamp fornecido pela classe datetime . Veja o código no editor.
#
# Resultado:
# Timestamp: 1601823300.0
#
# output
#
# A função timestamp devolve um valor float expressando o número de segundos decorridos entre a data e a hora indicada pelo objeto datetime e 1 de janeiro de 1970, 00:00:00 (UTC).


from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())