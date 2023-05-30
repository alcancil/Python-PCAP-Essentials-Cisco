# Os loops replace() .
#
# Por vezes pode ser necessário substituir o ano, mês, ou dia por um valor diferente. Não se pode fazer isto com os atributos de ano, mês e dia porque são apenas de leitura. Neste caso, pode utilizar o método # denominado replace.
#
# Execute o código no editor.
#
# Resultado:
# 1991-02-05
# 1992-01-16
#
# output
#
# Os parâmetros ano, mês e dia são opcionais. Pode passar apenas um parâmetro para o método replace , por exemplo, ano, ou todos os três como no exemplo.
# 
# O método replace devolve um objeto com data alterada, pelo que se deve lembrar de o atribuir a alguma variável.
#
# from datetime import date

from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

# Agora no padrão Brasileiro.

from datetime import date

d = date(1991, 2, 5)
date_formatado = d.strftime("%d/%m/%Y")
print(date_formatado)

d = d.replace(year=1992, month=1, day=16)
date_formatado = d.strftime("%d/%m/%Y")
print(date_formatado)
print()