# Análise de amostras de código
# Agora vamos mostrar-lhe alguns programas simples mas completos. Não os explicaremos em detalhe, porque consideramos os comentários (e os nomes das 
# variáveis) dentro do código guias suficientes.
#
# Todos os programas resolvem o mesmo problema - eles encontram o maior de vários números e imprimem-no.
#
# Exemplo 1:
#
# Vamos começar com o caso mais simples - como identificar o maior de dois números:
#
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)
#
#
# O snippet acima deve ser claro - ele lê dois valores inteiros, compara-os e descobre qual é o maior.
#
# Exemplo 2:
#
# Agora vamos mostrar-lhe um facto intrigante. O Python tem uma característica interessante, veja o código abaixo:
#
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)
#
#
# Nota: se algum dos ramos if-elif-else contiver apenas uma instrução, pode codificá-la de uma forma mais abrangente (não precisa de fazer uma linha 
# indentada após a keyword, mas apenas continuar a linha após os dois pontos).
#
# Este estilo, contudo, pode ser enganador, e não o vamos utilizar nos nossos futuros programas, mas vale definitivamente a pena saber se quiser ler e # compreender os programas de outra pessoa.
#
# Não há outras diferenças no código.
# 
# Exemplo 3:
#
# É altura de complicar o código - vamos encontrar o maior de três números. Será que vai ampliar o código? Um pouco.
#
# Assumimos que o primeiro valor é o maior. Em seguida, verificamos essa hipótese com os dois valores restantes.
#
# Veja o código abaixo:
#
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)
#
#
# Este método é significativamente mais simples do que tentar encontrar o maior número ao mesmo tempo, comparando todos os pares de números possíveis 
# (ou seja, o primeiro com o segundo, o segundo com o terceiro, o terceiro com o primeiro). Tente reconstruir o código por si mesmo.

