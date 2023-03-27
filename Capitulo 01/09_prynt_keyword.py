# A função print() - os argumentos de keyword
# O Python oferece outro mecanismo para a passagem de argumentos, que pode ser útil quando se quer convencer a print() função a 
# alterar um pouco o seu comportamento.
# Não o vamos explicar em profundidade neste momento. Planeamos fazê-lo quando falarmos de funções. Por agora, queremos simplesmente 
# mostrar-lhe como funciona. Sinta-se à vontade para o utilizar nos seus próprios programas.
# O mecanismo é chamado argumentos de keyword. O nome deriva do facto de o significado destes argumentos ser retirado não da sua localização 
# (posição) mas da palavra especial (keyword) utilizada para os identificar.
# A função print() tem dois argumentos de keyword que pode usar para os seus propósitos. O primeiro deles é nomeado end.
# Na janela do editor pode ver um exemplo muito simples da utilização de um argumento de keyword.
# Para a sua utilização, é necessário conhecer algumas regras:
#
# um argumento de keyword consiste em três elementos: uma keyword identificando o argumento (end aqui); um sinal de igual (=); 
# e um valor atribuído a esse argumento;
# qualquer argumento de keyword tem de ser colocado após o último argumento posicional (isto é muito importante)
#
# No nosso exemplo, fizemos uso do end argumento de keyword, e definimo-lo para uma string contendo um espaço.
#
# Execute o código para ver como ele funciona.
# A consola deve agora mostrar o seguinte texto:
#
# My name is Python. Monty Python.
# output
#
# Como pode ver, o argumento de keyword end determina os carateres que a função print() envia para o output, uma vez que atinge o 
# final dos seus argumentos posicionais.
#
# O comportamento padrão reflete a situação em que o argumento de keyword end é implicitamente usado da seguinte maneira: end="\n".


print("My name is", "Python.", end=" ")
print("Monty Python.")
