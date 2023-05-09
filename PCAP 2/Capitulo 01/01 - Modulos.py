# MODULARIZAÇÂO EM PYTHON
#
#
#  Quando começamos a escrever um código em python, a tendencia e que cada vez mais os codigos fiquem maiores e mais complexos. Porem, ficaria muito complicado escrever um programa inteiro utilizando se 
# somente um arquivo. Isso ficaria inivael pois tornaria o código muito dificil de se ler e tornaria impossivel de outras pessoas contribuirem com o mesmo. Então para solucionar esse tipo de situação,
# foram inventados os modulos em python. Por exemplo, vamos supor que você queira utilizar uma função que retorne a soma de a + b. Você poderia té criar essa funcao dentro do seu arquivo e depois chama-la
# em algum outro ponto. Mas uma abordagem que foi criada aqui funciona da seguinte maneira: a pessoa cria um arquivo contendo essa funcao e outras mais. Dessa maneira quando voce estiver escrevendo seu
# codigo, é possivel importar essa funcao que está dentro do outro arquivo ou mesmo carregar o conteudo completo desse arrquivo. Portanto, o python já vem modulos prontos dele ou você pode criar os seus
# proprios. Sempre e recomendado que se realize a importacao no inicio do codigo. Veja um exemplo disso.


import math
print(math.sin(math.pi/2))

# Nesse exemplo foi realizado a importacao da biblioteca math. Depois, ao importarmos todo o conteudo da biblioteca math, quando formos utiliza-la, precisamos dizer o que queremos utilizar dentro desse
# arquivo . Nesse caso, quando adicionamos o ponto . depois da palavra, estamos dizendo que queremos utilizar a funcao sin que está dentro da biblioteca math --->> (sin.math)
