# O Processador de Números
#
# O terceiro programa mostra um método simples que lhe permite introduzir uma linha cheia de números, e processá-los facilmente. Nota: a função de rotina input() , combinada juntamente com as funções int() ou # float() , é inadequada para esta finalidade.
#
# O processamento será extremamente fácil - queremos que os números sejam somados.
#
# Veja o código no editor. Vamos analisá-lo.
#
# A utilização da compreensão de lista pode tornar o código mais magro. Pode fazer isso se quiser.
#
# Vamos apresentar a nossa versão:
#
#    linha 03: pedir ao utilizador para introduzir uma linha preenchida com qualquer número de números (os números podem ser floats)
#    linha 04: dividir a linha recebendo uma lista de substrings;
#    linha 05: iniciar a soma total a zero;
#    linha 06: como a conversão de string-float pode levantar uma exceção, o melhor é continuar com a proteção do bloco try-except;
#    linha 07: iterar através da lista...
#    linha 08: ...e tentar converter todos os seus elementos em números float; se funcionar, aumentar a soma;
#    linha 09: tudo está bem até agora, por isso imprimir a soma;
#    linha 10: o programa termina aqui no caso de um erro;
#    linha 11: imprimir uma mensagem de diagnóstico mostrando ao utilizador o motivo da falha.
#
# O código tem um ponto fraco importante - apresenta um resultado falso quando o utilizador introduz uma linha vazia. Consegue consertá-lo?


# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")