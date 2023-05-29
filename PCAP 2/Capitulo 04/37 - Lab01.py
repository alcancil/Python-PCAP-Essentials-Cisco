# LAB
#
# Tempo estimado
#
# 30-60 minutos
# Nível de dificuldade
#
# Médio
# Objetivos
#
#    melhorar as competências do aluno no funcionamento com ficheiros (leitura)
#    utilizar coleções de dados para a contagem de dados numerosos.
#
# Cenário
#
# Um ficheiro de texto contém algum texto (nada de anormal) mas precisamos de saber com que frequência (ou quão rara) 
# cada letra aparece no texto. Tal análise pode ser útil na criptografia, por isso queremos ser capazes de o fazer em referência ao alfabeto latino.
#
# A sua tarefa é escrever um programa que:
#
#    pede ao utilizador o nome do ficheiro de input;
#    lê o ficheiro (se possível) e conta todas as letras latinas (letras minúsculas e maiúsculas são tratadas como iguais)
#    imprime um histograma simples em ordem alfabética (só devem ser apresentadas contagens não nulas)
#
# Crie um ficheiro de teste para o código, e verifique se o seu histograma contém resultados válidos.
#
# Assumindo que o ficheiro do teste contém apenas uma linha preenchida com:
# aBc
#
# samplefile.txt
#
# o output esperado deve ter a seguinte aparência:
# a -> 1
# b -> 1
# c -> 1
#
# output
#
# Dica: Achamos que um dicionário é um meio perfeito de recolha de dados para armazenar as contagens. As letras podem ser chaves enquanto os contadores podem ser valores.

def contar_letras(filename):
    frequencia = {}

    try:
        with open(filename, 'r') as file:
            texto = file.read()

            for letra in texto:
                if letra.isalpha():
                    letra = letra.lower()  # converter para minúscula
                    if letra in frequencia:
                        frequencia[letra] += 1
                    else:
                        frequencia[letra] = 1

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return

    for letra, count in sorted(frequencia.items()):
        print(letra, '->', count)


nome_arquivo = input("Digite o nome do arquivo de input: ")
contar_letras(nome_arquivo)
