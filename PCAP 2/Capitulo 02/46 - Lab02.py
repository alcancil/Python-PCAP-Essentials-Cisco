# LAB
#
# Tempo estimado
#
# 15-30 minutos
# Nível de dificuldade
#
# Fácil
# Objetivos
#
#    melhorar as habilidades do aluno a operar com strings;
#    encorajar o estudante a procurar soluções não óbvias.
#
# Cenário
#
# Sabe o que é um palíndromo?
#
# É uma palavra que parece a mesma quando lida para a frente e para trás. Por exemplo, "rever" é um palíndromo, enquanto "leal" não é.
#
# A sua tarefa é escrever um programa que:
#
#    pede ao utilizador algum texto;
#    verifica se o texto introduzido é um palíndromo, e imprime o resultado.
#
# Nota:
#
#    assuma que uma string vazia não é um palíndromo;
#    trate as letras maiúsculas e minúsculas como iguais;
#    os espaços não são tidos em conta durante a verificação - trate-os como inexistentes;
#    existem mais do que algumas soluções corretas - tente encontrar mais do que uma.
#
# Teste o seu código utilizando os dados por nós fornecidos.
# Dados de teste
#
# Input de amostra:
# Ten animals I slam in a net
#
# Exemplo de output:
# It's a palindrome
#
#
# Input de amostra:
# Eleven animals I slam in a net
#
# Exemplo de output:
# It's not a palindrome
#

frase = input("Digite uma frase, somente letras : ")
invertida = ""
#i = 0

# Como o python começa contando em 0 e a contagem reversa começa em -1, isso não pegaria o primeiro indice invertido
# A solução é indicar o indice 1 (começar na segunda letra) e no final somar + 1, o que daria o 0 invertido
for i in range(1, len(frase) + 1):
    invertida += frase[-i]
    
print(invertida)

if frase == invertida:
    print("É um PALINDROMO!!!")
else:
    print("Não é um PALINDROMO!!!")