# Os loops break e declarações continue : mais exemplos
# Voltemos ao nosso programa que reconhece o maior entre os números introduzidos. Iremos convertê-lo duas vezes, utilizando as instruções break e 
# continue .
#
# Analise o código, e julgue se e como utilizaria qualquer um deles.
#
# A variante break vai aqui:
#
print("Exemplo 01")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")

#
# Execute-a, teste-a e experimente com ela.
#
# E agora a variante continue :

print()
print("Exemplo 02 - Variante")
largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


# Olhe cuidadosamente, o utilizador introduz o primeiro número antes de o programa entrar no loop while . O número subsequente é inserido quando o 
# programa já está em loop.
#
# Novamente - execute o programa, teste-o e experimente com ele
