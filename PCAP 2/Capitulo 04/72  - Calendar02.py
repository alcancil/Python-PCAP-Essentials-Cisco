# O seu primeiro calendário
#
# Começará a sua aventura com o módulo calendar com uma função simples chamada calendar, que permite exibir o calendário para todo o ano. Vejamos como usá-lo para exibir o calendário de 2020. Execute o código # no editor e veja o que acontece.
#
# O resultado exibido é semelhante ao resultado do comando cal disponível em Unix. Se quiser alterar a formatação padrão do calendário, pode utilizar os seguintes parâmetros:
#
#    w – largura da coluna de data (default 2)
#    l – número de linhas por semana (default 1)
#    c — número de espaços entre as colunas do mês (default 6)
#    m — número de colunas (default 3)
#
# A função de calendário requer que se especifique o ano, enquanto que os outros parâmetros responsáveis pela formatação são opcionais. Encorajamo-lo a experimentar por si próprio estes parâmetros.

import calendar
print(calendar.calendar(2020))


# Uma boa alternativa à função acima é a função chamada prcal, que também toma os mesmos parâmetros que a função calendar , mas não requer o uso da função print para exibir o calendário. A sua utilização 
# assemelha-se a esta:

import calendar
calendar.prcal(2020)


# Imprimindo em pt/br

import calendar
import locale

# Definir a localização para português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Imprimir o calendário
print(calendar.calendar(2020))
