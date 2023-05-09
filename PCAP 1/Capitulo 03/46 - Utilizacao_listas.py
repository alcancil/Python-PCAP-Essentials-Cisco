# Utilização de listas
# O loop for tem uma variante muito especial que pode processar listas muito eficazmente - vejamos isso.
#
# Vamos supor que deseja calcular a soma de todos os valores armazenados na lista my_list .
#
# É necessária uma variável cuja soma será armazenada e à qual será inicialmente atribuído um valor de 0 - o seu nome será total. (Nota: não vamos nomeá-la sum visto o Python usar o mesmo nome para uma das 
# suas funções internas - sum(). Utilizar o mesmo nome seria geralmente considerado uma má prática). Em seguida, acrescenta-lhe todos os elementos da lista utilizando o loop for . Veja o snippet no editor.
#
# Vamos comentar este exemplo:
#
# à lista é atribuída uma sequência de cinco valores inteiros;
# a variável i toma os valores 0, 1, 2, 3, e 4, e depois indexa a lista, selecionando os elementos seguintes: o primeiro, o segundo, o terceiro, o quarto e o quinto;
# cada um destes elementos é adicionado em conjunto pelo operador += à variável total , dando o resultado final no fim do loop;
# observe a forma como a função len() foi utilizada - torna o código independente de quaisquer possíveis alterações no conteúdo da lista.
#
# A segunda face do loop for .
# Mas o loop for pode fazer muito mais. Pode ocultar todas as ações ligadas à indexação da lista, e entregar todos os elementos da lista de uma forma prática.
#
# Este snippet modificado mostra como isto funciona:
#
# my_list = [10, 1, 8, 3, 5]
# total = 0
#
# for i in my_list:
#    total += i
#
# print(total)
#
#
# O que acontece aqui?
#
# a instrução for especifica a variável usada para navegar na lista (i aqui) seguida pela keyword in e pelo nome da lista que está a ser processada (my_list aqui)
# à variável i são atribuídos os valores de todos os elementos da lista subsequente, e o processo ocorre tantas vezes quantos os elementos da lista;
# isto significa que se utiliza a variável i como uma cópia dos valores dos elementos, e não se precisa de utilizar índices;
# a função len() também não é necessária aqui.

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
