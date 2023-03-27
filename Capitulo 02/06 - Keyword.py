# O mecanismo é chamado argumentos de keyword. O nome deriva do facto de o significado destes argumentos ser retirado não da sua localização (posição) mas # da palavra especial (keyword) utilizada para os identificar.
# Para a sua utilização, é necessário conhecer algumas regras:
# 
# um argumento de keyword consiste em três elementos: uma keyword identificando o argumento (end aqui); um sinal de igual (=); e um valor atribuído a esse # argumento;
# qualquer argumento de keyword tem de ser colocado após o último argumento posicional (isto é muito importante)
#
print("My name is", "Python.", end=" ")
print("Monty Python.")

print("My name is", "Python.", end="\n")
print("Monty Python.")