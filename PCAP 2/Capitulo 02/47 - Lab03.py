# LAB
#
# Tempo estimado
#
# 30-60 minutos
# Nível de dificuldade
#
# Fácil
# Objetivos
#
#    melhorar as habilidades do aluno a operar com strings;
#    converter strings em listas, e vice-versa.
#
# Cenário
#
# Um anagrama é uma nova palavra formada pelo rearranjo das letras de uma palavra, usando todas as letras originais exatamente uma vez. Por exemplo, as frases “o bom programa” e “agarram o pombo” são 
# anagramas, enquanto “Eu sou” e “Você é” não são.
#
# A sua tarefa é escrever um programa que:
#
#    pede ao utilizador dois textos separados;
#    verifica se os textos introduzidos são anagramas e imprime o resultado.
#
# Nota:
#
#    assuma que duas strings vazias não são anagramas;
#    trate as letras maiúsculas e minúsculas como iguais;
#    os espaços não são tidos em conta durante a verificação - trate-os como inexistentes
#
# Teste o seu código utilizando os dados por nós fornecidos.
# Dados de teste
#
# Input de amostra:
# Listen
# Silent
#
# Exemplo de output:
# Anagrams
#
#
# Input de amostra:
# modern
# norman
#
# Exemplo de output:
# Not anagrams


def is_anagram(word1, word2):
    # Remove espaços em branco e converte todas as letras para minúsculas
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Verifica se as palavras têm o mesmo comprimento
    if len(word1) != len(word2):
        return False

    # Verifica se as palavras contêm as mesmas letras
    for letter in word1:
        if letter not in word2:
            return False
        else:
            # Remove a letra de word2 para evitar contagens duplicadas
            word2 = word2.replace(letter, "", 1)

    return True

# Pedir ao usuário para inserir duas palavras
word1 = input("Insira a primeira palavra: ")
word2 = input("Insira a segunda palavra: ")

# Verificar se as palavras são anagramas e imprimir o resultado
if is_anagram(word1, word2):
    print("As palavras são anagramas.")
else:
    print("As palavras não são anagramas.")