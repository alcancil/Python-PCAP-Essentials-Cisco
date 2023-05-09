# Algumas palavras sobre None
# Deixe-nos apresentar-lhe um valor muito curioso (para sermos honestos, um valor nulo), chamado None.
#
# Os seus dados não representam nenhum valor razoável - na verdade, não é um valor de todo; portanto, não deve tomar parte em nenhuma expressão.
#
# Por exemplo, um snippet como este:
#
# print(None + 2)
#
#
# causará um erro de runtime, descrito pela seguinte mensagem de diagnóstico:
#
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# output
#
#
# Nota: None é uma keyword.
#
# Existem apenas dois tipos de circunstâncias onde None pode ser utilizado em segurança:
#
# quando o atribui a uma variável (ou o devolve como o resultado de uma função)
# quando o compara com uma variável para diagnosticar o seu estado interno.
# Tal como aqui:
#
# value = None
# if value is None:
#    print("Sorry, you don't carry any value")
#
#
# Não se esqueça disto: se uma função não devolver um determinado valor usando uma return cláusula de expressão, supõe-se que ela devolve implicitamente None.
#
# Vamos testá-lo.

def sacanagem():
   value = None
   if value is None:
     print("Sorry, you don't carry any value")
    
print(sacanagem())