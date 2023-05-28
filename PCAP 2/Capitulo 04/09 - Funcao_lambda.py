# A função lambda .
#
# A função lambda é um conceito emprestado da matemática, mais especificamente, de uma parte chamada cálculo Lambda, mas estes dois fenómenos não são a mesma coisa.
#
# Os matemáticos utilizam o cálculo Lambda em muitos sistemas formais ligados à lógica, recorrência, ou provabilidade do teorema. Os programadores usam a função lambda para simplificar o código, para 
# torná- lo mais claro e mais fácil de entender.
#
# Uma função lambda é uma função sem nome (também se pode chamar-lhe uma função anónima). Evidentemente, tal afirmação levanta imediatamente a questão: como utilizar qualquer coisa que não possa ser 
# identificada?
#
# Felizmente, não é um problema, pois pode nomear tal função se realmente precisar, mas, de facto, em muitos casos, a função lambda pode existir e trabalhar enquanto permanece totalmente incógnita.
#
# A declaração da função lambda não se assemelha a uma declaração de função normal de forma alguma - veja por si mesmo:
# lambda parameters: expression
#
#
# Tal cláusula devolve o valor da expressão quando se tem em conta o valor atual do atual argumento lambda .
#
# Como de costume, um exemplo será útil. O nosso exemplo usa três funções lambda , mas dá-lhes nomes. Olhe com atenção:

two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

#
#
#
# Vamos analisá-lo:
#
#    a primeira lambda é uma função anónima sem parâmetros que devolve sempre 2. Como a atribuímos a uma variável chamada two, podemos dizer que a função já não é anónima, e podemos usar o nome para a 
# invocar.
#
#    a segunda é uma função anónima de um parâmetro que devolve o valor do seu argumento ao quadrado. Também a nomeámos como tal.
#
#    a terceira lambda toma dois parâmetros e devolve o valor do primeiro elevado à potência do segundo. O nome da variável que transporta a lambda fala por si. Não utilizamos pow para evitar confusão com a # função integrada do mesmo nome e do mesmo objetivo.
#
# O programa produz o seguinte output:
# 4 4
# 1 1
# 0 0
# 1 1
# 4 4
#
# output
#
# Este exemplo é suficientemente claro para mostrar como lambdasão declaradas e como se comportam, mas não diz nada sobre o porquê de serem necessárias, e para que são usadas, uma vez que todas elas podem 
# ser substituídas por funções Python de rotina.
#
# Onde está o benefício?

