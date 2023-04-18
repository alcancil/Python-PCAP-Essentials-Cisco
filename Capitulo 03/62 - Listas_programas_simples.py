# Listas - alguns programas simples
# Agora vamos encontrar a localização de um dado elemento dentro de uma lista:
#
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


# Nota:
#
# o valor alvo é armazenado na variável to_find ;
# o estado atual da pesquisa é armazenado na variável found (True/False)
# quando found se torna True, o loop for é saído.
# Vamos supor que escolheu os seguintes números na lotaria: 3, 7, 11, 42, 34, 49.
#
# Os números que foram sorteados são: 5, 11, 9, 42, 3, 49.
#
# A questão é: em quantos números é que acertou?
#
# O programa dar-lhe-á a resposta:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


# Nota:
#
# a keyword drawn armazena todos os números sorteados;
# a lista bets armazena as suas apostas;
# a variável hits conta os seus êxitos.
# O output do programa é: 4.