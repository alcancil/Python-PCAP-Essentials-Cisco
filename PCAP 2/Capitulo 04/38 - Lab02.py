# LAB
#
# Tempo estimado
#
# 15-30 minutos
# Nível de dificuldade
#
# Médio
# Pré-requisitos
#
# 4.3.1.15
# Objetivos
#
#    melhorar as capacidades do aluno em operar com ficheiros (leitura/escrita)
#    utilizar lambdas para alterar a ordem de classificação.
#
# Cenário
#
# O código anterior precisa de ser melhorado. Está tudo bem, mas tem de ser melhor.
#
# A sua tarefa é fazer algumas alterações, que geram os seguintes resultados:
#
#    o histograma de output será ordenado com base na frequência dos carateres (o contador maior deve ser apresentado primeiro)
#    o histograma deve ser enviado para um ficheiro com o mesmo nome que o de input, mas com o sufixo '.hist' (deve ser concatenado com o nome original)
#
# Assumindo que o ficheiro de input contém apenas uma linha preenchida:
# cBabAa
#
# samplefile.txt
#
# o output esperado deve ter a seguinte aparência:
# a -> 3
# b -> 2
# c -> 1
#
# output
#
# Dica: Use um lambda para alterar a ordem de classificação.

def generate_histogram(filename):
    # Ler o arquivo
    with open(filename, 'r') as file:
        text = file.read()

    # Contar a frequência dos caracteres
    char_count = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1

    # Ordenar o histograma com base na frequência dos caracteres
    sorted_hist = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

    # Gerar o nome do arquivo de saída com o sufixo '.hist'
    output_filename = filename + '.hist'

    # Escrever o histograma no arquivo de saída
    with open(output_filename, 'w') as file:
        for char, count in sorted_hist:
            file.write(f"{char} -> {count}\n")

    print(f"Histograma gerado e salvo no arquivo '{output_filename}'.")

# Solicitar o nome do arquivo de input ao usuário
filename = input("Digite o nome do arquivo de input: ")

# Gerar o histograma
generate_histogram(filename)
