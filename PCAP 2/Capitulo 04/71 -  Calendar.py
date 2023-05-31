
Introdução ao módulo calendar .

Para além dos módulos datetime e time , a biblioteca padrão Python fornece um módulo chamado calendar que, como o nome sugere, oferece funções relacionadas com o calendário.

Uma delas é, evidentemente, a exibição do calendário. É importante que os dias da semana sejam exibidos de segunda a domingo, e cada dia da semana tenha a sua representação sob a forma de um número inteiro:
Dia da semana 	Valor inteiro 	Constante
Segunda-feira 	0 	calendar.MONDAY
Terça-feira 	1 	calendar.TUESDAY
Quarta-feira 	2 	calendar.WEDNESDAY
Quinta-feira 	3 	calendar.THURSDAY
Sexta-feira 	4 	calendar.FRIDAY
Sábado 	5 	calendar.SATURDAY
Domingo 	6 	calendar.SUNDAY

A tabela acima mostra a representação dos dias da semana no módulo calendar . O primeiro dia da semana (segunda-feira) é representado pelo valor 0 e pela constante calendar.MONDAY, enquanto que o último dia da semana (domingo) é representado pelo valor 6 e pela constante calendar.SUNDAY.



Uma cobra e um calendário


Para os meses, os valores inteiros são indexados a partir de 1, ou seja, janeiro é representado por 1, e dezembro por 12. Infelizmente, não há constantes que expressem os meses.

As informações acima referidas ser-lhe-ão úteis quando trabalhar com o módulo calendar nesta parte do curso, mas primeiro vamos começar com alguns exemplos simples de calendário.