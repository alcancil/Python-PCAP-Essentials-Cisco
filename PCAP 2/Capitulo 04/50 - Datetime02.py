# Obter a data local atual e criar objetos de data
#
# Uma das classes fornecidas pelo módulo datetime é uma classe chamada date. Os objetos desta classe representam uma data que consiste no ano, mês e dia. Veja o código no editor para ver como é na prática e 
# obter a data local atual usando o today método.
#
# Execute o código para ver o que acontece.
#
# O método today devolve um objeto date que representa a data local atual. Note-se que o objeto date tem três atributos: ano, mês e dia.
#
# Tenha cuidado, pois estes atributos são apenas de leitura. Para criar um objeto date , deve passar os parâmetros de ano, mês e dia como se segue:
#
# from datetime import date
#
# my_date = date(2019, 11, 4)
# print(my_date)
#
# Execute o exemplo para ver o que acontece.
#
# Ao criar um objeto de data, tenha em mente as seguintes restrições:
# Parâmetro 	Restrições
# year 	
#
# O parâmetro ano deve ser maior ou igual a 1 (constante MINYEAR) e menor ou igual a 9999 (constante MAXYEAR).
# month 	
#
# O parâmetro mês deve ser maior ou igual a 1 e menor ou igual a 12.
# day 	
#
# O parâmetro dia deve ser maior ou igual a 1 e menor ou igual ao último dia do mês e ano em questão.
# 
# Nota: Mais tarde neste curso aprenderá a alterar o formato padrão da data.

from datetime import date

today = date.today()

print("Data em formato americano.")
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print()

# Vamos converter o código para exibir no formato brasileiro

from datetime import date

hoje = date.today()

hoje_formatado = hoje.strftime("%d/%m/%Y")

print("Data no formato BRASILEIRO")
print("Hoje:", hoje_formatado.encode('latin-1').decode('latin-1'))
print("Dia:", hoje.day)
print("Mês:", hoje.month)
print("Ano:", hoje.year)


# Neste código, utilizamos o método strftime para formatar a data hoje. Passamos o formato desejado "%d/%m/%Y" como argumento para strftime, onde:
#
# %d representa o dia com dois dígitos (por exemplo, 01, 02, ..., 31)
# %m representa o mês com dois dígitos (por exemplo, 01, 02, ..., 12)
# %Y representa o ano com quatro dígitos (por exemplo, 2021, 2022, ...)
# O resultado formatado é armazenado na variável hoje_formatado e é exibido na tela juntamente com o dia, mês e ano separadamente.
#
# Agora, a saída será exibida no formato brasileiro de Dia, Mês e Ano.