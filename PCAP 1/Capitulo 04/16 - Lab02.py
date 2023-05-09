# LAB
#
# Tempo estimado
# 
# 15-20 minutos
# Nível de dificuldade
#
# Médio
# Pré-requisitos
#
# LAB 4.3.1.6
# Objetivos
#
# Familiarizar o aluno a:
#
#    projetar e escrever funções parametrizadas;
#    utilizar a return declaração;
#    utilizar as próprias funções do aluno.
#
# Cenário
#
# A sua tarefa é escrever e testar uma função que toma dois argumentos (um ano e um mês) e devolve o número de dias para o par mês/ano dado (enquanto apenas fevereiro é sensível ao valor year , a sua função 
# deve ser universal).
#
# A parte inicial da função está pronta. Agora, convença a função a devolver None se os seus argumentos não fizerem sentido.
#
# É claro que pode (e deve) usar a função previamente escrita e testada (LAB 4.3.1.6). Pode ser muito útil. Encorajamo-lo a utilizar uma lista preenchida com a duração dos meses. Pode criá-la dentro da 
# função - este truque irá encurtar significativamente o código.
#
# Preparámos um código de teste. Expanda-o para incluir mais casos de teste.

def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)  # Código do lab anterior

def days_in_month(year, month):
    #Código novo
    days_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month < 1 or month > 12:
        return None  # retorna None caso o mês seja inválido
    if is_year_leap(year) == 2:
       return 29 
    else :
       return days_per_month[month - 1]
    #Fim do código

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]: