# Mais sobre exceções
#
# O bloco try-except pode ser prolongado de mais uma forma - adicionando uma parte encabeçada pela keyword finally (deve ser o último ramo do código concebido para lidar com exceções).
#
# Nota: estas duas variantes (else e finally) não são de modo algum dependentes, e podem coexistir ou ocorrer independentemente.
#
# O bloco finally é sempre executado (finaliza a execução do bloco try-except, daí o seu nome), independentemente do que aconteceu anteriormente, mesmo quando se levanta uma exceção, independentemente de esta # ter sido tratada ou não.
#
# Veja o código no editor. O seu output é:
# Everything went fine
# It's time to say good bye
# 0.5
# Division failed
# It's time to say good bye
# None


def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))

