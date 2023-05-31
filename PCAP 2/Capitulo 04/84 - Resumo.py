
# Key takeaways
#
# 1. no módulo calendar , os dias da semana são exibidos de segunda-feira a domingo. Cada dia da semana tem a sua representação sob a forma de um número inteiro, onde o primeiro dia da semana (segunda-
# feira) é representado pelo valor 0, enquanto o último dia da semana (domingo) é representado pelo valor 6.
#
# 2. Para exibir um calendário para qualquer ano, chame a função calendar com o ano passado como seu argumento, por exemplo:
#
import calendar
print(calendar.calendar(2020))
print()

# Nota: Uma boa alternativa para a função acima é a função chamada prcal, que também toma os mesmos parâmetros que a função calendar , mas não requer o uso da função print para exibir o calendário.
#
# 3. Para exibir um calendário para qualquer mês do ano, chame a função month , passando ano e mês para ela. Por exemplo:
# 
import calendar
print(calendar.month(2020, 9))
print()

# Nota: Também pode utilizar a função prmonth , que tem os mesmos parâmetros que a função month , mas não requer o uso da função print para exibir o calendário.
#
# 4. O objeto da exceção setfirstweekday permite-lhe alterar o primeiro dia da semana. Toma um valor de 0 a 6, onde 0 é domingo e 6 é sábado.
#
# 5. O resultado da função weekday é um dia da semana como um valor inteiro para um determinado ano, mês e dia:
#
import calendar
print(calendar.weekday(2020, 9, 29)) # This displays 1, which means Tuesday.
print()

# 6. A função weekheader devolve os nomes dos dias da semana numa forma abreviada. O método weekheader exige que especifique a largura em carateres para um dia da semana. Se a largura que fornecer for 
# superior a 3, ainda receberá os nomes abreviados dos dias da semana compostos por apenas três carateres. Por exemplo:
#
import calendar
print(calendar.weekheader(2)) # This display: Mo Tu We Th Fr Sa Su
print()


# 7. Uma função muito útil disponível no módulo calendar é a função chamada isleap, que, como o nome sugere, permite verificar se o ano é um ano bissexto ou não:
#
import calendar
print(calendar.isleap(2020)) # This displays: True
print()

# 8. Pode criar um objeto calendar você mesmo usando a classe Calendar , que, ao criar o seu objeto, lhe permite alterar o primeiro dia da semana com o parâmetro opcional firstweekday , por exemplo:

import calendar  

c = calendar.Calendar(2)

for weekday in c.iterweekdays():
    print(weekday, end=" ")

print()

# Result: 2 3 4 5 6 0 1

# O iterweekdays devolve um iterador para números de dias úteis. O primeiro valor devolvido é sempre igual ao valor da propriedade firstweekday .



# Exercício 1
#
# Qual é o output do seguinte snippet?

import calendar
print(calendar.weekheader(1))

# M T W T F S S


# Exercício 2
#
# Qual é o output do seguinte snippet?

import calendar  

c = calendar.Calendar()

for weekday in c.iterweekdays():
    print(weekday, end=" ")

# 0 1 2 3 4 5 6
