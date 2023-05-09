# Nesse exemplo, foi criado um arquivo na mesma pasta do arquivo 01 - Modulos02.py, que é o nosso codigo principal, contendo duas funcoes e uma constatnte chamadad idade. Quando queremos utilizar
# algumas dessas funcoes, nos realizamos a importacao do modulo como no exemplo:  

import utils 

print(utils.soma(2, 3))
print(utils.divisao(12, 3))
print(utils.idade)

# Ao realizar a importacao chamando import nome_do_modulo, nos estamos chamando todo o conteudo do modulo. Depois, quando formos utilizar alguma funcao que está contida dentro de utils, por exemplo, 
# precisamos invocar o nome do modulo.o_conteudi_que_se_quer_chamar. Exemplo: utils.idade 