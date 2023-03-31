# Função IF else
#
# A função IF responde somente a uma condição. Por exemplo:
# Hoje está chovendo ? 
# Sim ou não --- você só pode escolher uma opção
#
# Vamos analisar o código:
#
# num = input("Digite um número de 0 a 9: ")
# if int(num) <= 9:
#    print("O numero escolhido esta entre 0 e 9")
#
# Aqui é pedido para escolher um número entre 0 e 9. Logo após é impresso assim:
# O número escolhido esta entre 0 e 19
#
# Mas e se escolhessemos digitar 10 ou algum outro número maior do que 9 ?
#
# Ai teríamos uma segunda opção que é contrária da que foi pedida.
#
# Então a funcao if() também pode ser usada com o senão else()
num = input("Digite um número de 0 a 9: ")
if int(num) <= 9:
   print("O numero escolhido esta entre 0 e 9")
else:
   print("O numero escolhido e maior do 9 !! Opcao errada.")
#
# OBS: o else também trabalha com o mesmo esquema de identacao que o IF
# OBS: depois de cada if ou else é necessario digitar : 