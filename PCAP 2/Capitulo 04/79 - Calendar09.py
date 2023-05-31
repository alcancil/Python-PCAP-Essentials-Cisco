# Criar um objeto Calendar .
#
# O construtor de classes Calendar toma um parâmetro opcional chamado firstweekday, por defeito igual a 0 (segunda-feira).
#
# O parâmetro firstweekday deve ser um inteiro entre 0-6. Para este efeito, podemos utilizar as constantes já conhecidas - ver o código no editor.
#
# O programa fará output do seguinte resultado:
# 6 0 1 2 3 4 5
#
# output
#
# O exemplo de código usa o método de classe Calendar chamado iterweekdays, que devolve um iterador para os números dos dias da semana.
#
# O primeiro valor devolvido é sempre igual ao valor da propriedade firstweekday . Visto no nosso exemplo o primeiro valor devolvido ser 6, isso significa que a semana começa num domingo.

import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
