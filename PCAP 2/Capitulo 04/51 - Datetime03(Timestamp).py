# Criar um objeto de data a partir de um timestamp
#
# A classe date dá-nos a capacidade de criar um objeto de data a partir de um timestamp.
#
# Em Unix, o timestamp expressa o número de segundos desde 1 de janeiro de 1970, 00:00:00 (UTC). Esta data é chamada a época Unix, porque foi quando a contagem do tempo começou nos sistemas Unix.
#
# O timestamp é na realidade a diferença entre uma determinada data (incluindo a hora) e 1 de janeiro de 1970, 00:00:00 (UTC), expressa em segundos.
#
# Para criar um objeto de data a partir de um timestamp, temos de passar um timestamp Unix para o método fromtimestamp .
#
# Para este fim, podemos usar o módulo time , que fornece funções relacionadas ao tempo. Uma delas é uma função chamada time() que devolve o número de segundos desde 1 de janeiro de 1970 até ao momento atual # sob a forma de um número float. Dê uma vista de olhos no exemplo no editor.
#
# Execute o código para ver o output.
#
# Se executar o código de amostra várias vezes, poderá ver como o timestamp se incrementa a si próprio. Vale a pena acrescentar que o resultado da função time depende da plataforma, porque nos sistemas Unix e # Windows, os segundos bissextos não são contados.
#
# Nota: Nesta parte do curso falaremos também sobre o módulo time.

# Timestamp no formato AMERICANO

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)
print()

# Timestamp no formato Brasileiro

from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
date_formatado = d.strftime("%d/%m/%Y")
print("Data:", date_formatado)
