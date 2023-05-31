# Métodos que devolvem a data e hora atuais
#
# A classe datetime tem vários métodos que devolvem a data e hora atuais. Estes métodos são:
#
#    today() — devolve a data e hora locais atuais com o atributo tzinfo definido para None;
#    now() — devolve a data e hora local atuais, tal como o método today, a menos que lhe passemos o argumento opcional tz. O argumento deste método deve ser um objeto da subclasse tzinfo;
#    utcnow() — devolve a data e hora UTC atuais com o atributo tzinfo definido para None.
#
# Execute o código no editor para os ver a todos na prática. O que pode dizer sobre o output?
#
# Como pode ver, o resultado de todos os três métodos é o mesmo. As pequenas diferenças são causadas pelo tempo decorrido entre chamadas subsequentes.
#
# Nota: Pode ler mais sobre os objetos tzinfo na documentação.

# Formato Americano

from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())
print()

# Formato Brasileiro.

from datetime import datetime
import locale

# Definir a localização como "pt_BR" (português do Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR')

data_atual = datetime.today()
data_atual_formatada = data_atual.strftime("%d/%m/%Y")
print("Hoje:", data_atual_formatada)

data_agora = datetime.now()
data_agora_formatada = data_agora.strftime("%d/%m/%Y %H:%M:%S")
print("Agora:", data_agora_formatada)

data_utc = datetime.utcnow()
data_utc_formatada = data_utc.strftime("%d/%m/%Y %H:%M:%S")
print("UTC Agora:", data_utc_formatada)
