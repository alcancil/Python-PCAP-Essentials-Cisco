# Modulos
#
# Ja vimos que e possivel se criar um arquivo de modulos contendo funcoes, constantes, etc, para que possam ser importados dentro do codigo principal. Para isso, realizamos a importacao da seguinte maneira
# import utils. Mas isso tem um pequeno problema. Se o arquivo utils for grande, dessa forma estamos importando todo seu conteudo e assim, podemos causar algum impacto dentro da pareformance do programa final
# E se quisermos importar somete alguma funcao de dentro desse modulo por exemplo ? Veja o exemplo:


from utils import soma

print(soma(2,3))

# Perceba que agora importamos somente a funcao soma e deixamos sem importar a funcao divisao e nem a constatnet idade. 
#
# Obs: se mesmo assim quisermos importar todo o contudo de utils, basta utilizar *. Exemplo: import utils *
# Obs2: se quisermos importar mais algo de utils, basta utiliza a , . Exemplo: import utils soma, idade
