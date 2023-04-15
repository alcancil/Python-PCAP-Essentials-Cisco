# Key takeaways
#
# 1. Existem dois tipos de loops em Python: while e for:
#
# o loop while executa uma declaração ou um conjunto de declarações, desde que uma condição booleana especificada seja verdadeira, por exemplo:
#
# Example 1
while True:
    print("Stuck in an infinite loop.")

# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

#
# o loop for executa um conjunto de declarações várias vezes; é usado para iterar sobre uma sequência (por exemplo, uma lista, um dicionário, um tuple, # ou um conjunto - aprenderá sobre eles em breve) ou outros objetos que são iteráveis (por exemplo, strings). Pode utilizar o loop for para iterar 
# sobre uma sequência de números usando a função range . Veja os exemplos em baixo:
#
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")

# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)

#
# 2. Pode utilizar as declarações break e continue para alterar o fluxo de um loop:
#
# Utilize break para sair de um loop, por exemplo:
#
text = "OpenEDG Python Institute"
for letter in text:
    if letter == "P":
        break
    print(letter, end="")


# Utilize continue para ignorar a iteração atual e continuar com a próxima iteração, por exemplo:
#
text = "pyxpyxpyx"
for letter in text:
    if letter == "x":
        continue
    print(letter, end="")


#
#
#
# 3. Os loops while e for também podem ter uma cláusula else em Python. A cláusula else executa-se após o loop terminar a sua execução, desde que não 
# tenha sido terminado por break, por exemplo.:
#
n = 0

while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()

for i in range(0, 3):
    print(i)
else:
    print(i, "else")


# 4. O objeto da exceção range() gera uma sequência de números. Aceita números inteiros e devolve objetos de range. A sintaxe de range() parece como se # segue: range(start, stop, step), onde:
#
# start é um parâmetro opcional que especifica o número inicial da sequência (0 por padrão)
# stop é um parâmetro opcional que especifica o fim da sequência gerada (não está incluído),
# e step é um parâmetro opcional que especifica a diferença entre os números na sequência (1 por padrão.)
# Código de exemplo:

for i in range(3):
    print(i, end=" ")  # Outputs: 0 1 2

for i in range(6, 1, -2):
    print(i, end=" ")  # Outputs: 6, 4, 2

