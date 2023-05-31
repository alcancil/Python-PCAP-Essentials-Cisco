# Os loops weekheader() .
#
# Já deve ter reparado que o calendário contém cabeçalhos semanais de forma abreviada. Se necessário, pode obter nomes curtos de dias de semana usando o método weekheader .
#
# O método weekheader exige que especifique a largura em carateres para um dia da semana. Se a largura que fornecer for superior a 3, ainda receberá os nomes abreviados dos dias da semana compostos por três
# carateres.
#
# Vejamos então como obter um cabeçalho mais pequeno. Execute o código no editor.
#
# Resultado:
# Mo Tu We Th Fr Sa Su
#
# output
#
# Nota: Se mudar o primeiro dia da semana, por exemplo, utilizando a função setfirstweekday , afetará o resultado da função weekheader .


import calendar
print(calendar.weekheader(2))
