# Geradores - onde encontrá-los
#
# Gerador - a que associa esta palavra? Talvez se refira a algum dispositivo eletrónico. Ou talvez se refira a uma máquina pesada e séria concebida para produzir energia, elétrica ou outra.
#
# Um gerador Python é uma peça de código especializado capaz de produzir uma série de valores, e de controlar o processo de iteração. É por isso que os geradores são muitas vezes chamados iteradores, e embora # alguns possam encontrar uma distinção muito subtil entre estes dois, vamos tratá-los como um só.
#
# Pode não se aperceber, mas já encontrou geradores muitas, muitas vezes antes. Veja este snippet muito simples:

for i in range(5):
    print(i)


# A função range() é, de facto, um gerador, que é (de facto, mais uma vez) um iterador.
#
# Qual é a diferença?
#
# Uma função devolve um valor bem definido - pode ser o resultado de uma avaliação mais ou menos complexa de, por exemplo, um polinómio, e é invocada uma vez - apenas uma vez.
#
# Um gerador devolve uma série de valores e, em geral, é (implicitamente) invocado mais de uma vez.
#
# No exemplo, o gerador range() é invocado seis vezes, fornecendo cinco valores subsequentes de zero a quatro, e finalmente sinalizando que a série está completa.
#
# O processo acima é completamente transparente. Vamos lançar alguma luz sobre ele. Vamos mostrar-lhe o protocolo iterador.