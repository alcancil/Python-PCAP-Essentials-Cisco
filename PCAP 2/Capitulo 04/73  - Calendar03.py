# Calendário para um mês específico
#
# O módulo calendar tem uma função chamada month, que permite exibir um calendário para um mês específico. A sua utilização é muito simples, apenas precisa de especificar o ano e o mês - verifique o código no 
# editor.
#
# O exemplo exibe o calendário para novembro de 2020. Como na função calendar , pode alterar a formatação padrão usando os seguintes parâmetros:
#
#    w – largura da coluna de data (default 2)
#    l – número de linhas por semana (default 1)
#
# Nota: Também pode usar a função prmonth , que tem os mesmos parâmetros que a função month , mas não exige que use a função print para exibir o calendário.
#
# Em Inglês

import calendar
print(calendar.month(2020, 11))
print

# Em portuguÊs

import calendar
import locale

# Configurar a localização para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Imprimir o calendário em português
print(calendar.month(2020, 11))