# Os loops setfirstweekday() .
#
# Como já sabe, por defeito no módulo calendar , o primeiro dia da semana é segunda-feira. No entanto, pode alterar este comportamento usando uma função chamada setfirstweekday.
#
# Lembra-se da tabela que mostra os dias da semana e a sua representação sob a forma de valores inteiros? É altura de a utilizar, porque o módulo setfirstweekday requer um parâmetro expressando o dia da 
# semana sob a forma de um valor inteiro. Dê uma vista de olhos no exemplo no editor.
#
# O exemplo utiliza a constante calendar.SUNDAY , que contém um valor de 6. Claro que pode passar esse valor diretamente para a função setfirstweekday , mas a versão com uma constante é mais elegante.
#
# Como resultado, obtemos um calendário mostrando o mês de dezembro de 2020, no qual o primeiro dia de todas as semanas é domingo.


import calendar

calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)