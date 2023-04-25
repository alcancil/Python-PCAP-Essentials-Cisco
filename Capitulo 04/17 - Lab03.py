# LAB
#
# Tempo estimado
#
# 20-30 minutos
# Nível de dificuldade
#
# Médio
# Pré-requisitos
#
# LAB 4.3.1.6
# LAB 4.3.1.7
# Objetivos
# 
# Familiarizar o aluno a:
# 
#     projetar e escrever funções parametrizadas;
#     utilizar a return declaração;
#     construir um conjunto de funções de utilidade;
#     utilizar as próprias funções do aluno.
#
# Cenário
# 
# A sua tarefa consiste em escrever e testar uma função que toma três argumentos (um ano, um mês e um dia do mês) e devolve o dia correspondente do ano, ou devolve None se algum dos argumentos for inválido.
# 
# Use as funções previamente escritas e testadas. Adicione alguns casos de teste ao código. Este teste é apenas um começo.

def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
#
    days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month < 1 or month > 12:
        return None  # retorna None caso o mês seja inválido
    if is_year_leap(year) == 2:
       return 29 
    else :
       return days_per_month[month - 1]
    
def day_of_year(year, month, day):
#
# Write your new code here.
#   
    if month < 1 or month > 12 or day < 1:
        return None  # retorna None caso os parâmetros sejam inválidos
    total_days = day
    for m in range(1, month):
        month_days = days_in_month(year, m)
        if month_days is None:
            return None  # retorna None caso o mês informado seja inválido
        total_days += month_days
    if total_days > 365 and not is_year_leap(year):
        return None  # retorna None se o dia do ano ultrapassar 365 e o ano não é bissexto
    return total_days

# adicionando alguns casos de teste
test_years = [1900, 2000, 2020, 1987, 2022, 2023]
test_months = [2, 2, 12, 11, 2, 11]
test_days = [28, 29, 31, 30, 28, 25]
test_results = [59, 60, 366, 334, 59, 329]

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    dy = test_days[i]
    print("Teste", i+1, ": (ano, mês, dia) = ({},{},{})".format(yr, mo, dy))
    result = day_of_year(yr, mo, dy)
    if result == test_results[i]:
        print("Resultado esperado:", test_results[i], "- OK")
print(day_of_year(2000, 12, 31))