# Como a função input( ) recebe um string, não podemos realizar nenhum tipo de cálculo com o dado fornecido.
# Para cálculos utilizamos Inteiros ou FLoat
# Para isso existe uma solução. Acompanhe o exemplo:
#
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
#
# Nesse exemplo, estamos convertendo a string recebida no imput para float. Assim é possível se utilizar uma entrada do input( ) em cálculos.