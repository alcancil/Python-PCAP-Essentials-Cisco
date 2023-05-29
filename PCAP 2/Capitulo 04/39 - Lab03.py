# LAB
#
# Tempo estimado
#
# 30-90 minutos
# Nível de dificuldade
#
# Médio
# Objetivos
#
#    melhorar as competências do aluno em operar com ficheiros (leitura)
#    aperfeiçoar as capacidades do aluno na definição e utilização de exceções e dicionários auto-definidos.
#
# Cenário
#
# O Prof. Jekyll realiza aulas com os estudantes e faz regularmente anotações num ficheiro de texto. Cada linha do ficheiro contém três elementos: o primeiro nome do estudante, o último nome do estudante, e o # número de pontos que o estudante recebeu durante certas aulas.
#
# Os elementos são separados por espaços em branco. Cada estudante pode aparecer mais de uma vez no ficheiro do Prof. Jekyll.
#
# O ficheiro pode ter a seguinte aparência:
# John	Smith	      5
# Anna	Boleyn	4.5
# John	Smith	      2
# Anna	Boleyn	11
# Andrew	Cox	      1.5
# 
# samplefile.txt
#
# A sua tarefa é escrever um programa que:
#
#    pergunta ao utilizador o nome do ficheiro do Prof. Jekyll;
#    lê o conteúdo do ficheiro e conta a soma dos pontos recebidos por cada estudante;
#    imprime um relatório simples (mas ordenado), tal como este:
#
# Andrew Cox 	 1.5
# Anna Boleyn 	 15.5
# John Smith 	 7.0
#
# output
#
# Nota:
#
#    o seu programa deve ser totalmente protegido contra todas as falhas possíveis: a inexistência do ficheiro, o vazio do ficheiro, ou qualquer falha nos dados introduzidos; o encontro de qualquer erro de 
# dados deve causar a terminação imediata do programa, e o erro deve ser apresentado ao utilizador;
#    implemente e utilize a sua própria hierarquia de exceções - apresentámo-la no editor; a segunda exceção deve ser levantada quando uma linha má é detetada, e a terceira quando o source file existe mas 
# está vazio.
#
# Dica: Utilize um dicionário para armazenar os dados dos estudantes.

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


def process_student_data(filename):
    try:
        # Abrir o arquivo
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Verificar se o arquivo está vazio
        if len(lines) == 0:
            raise FileEmpty("O arquivo está vazio.")

        # Criar um dicionário para armazenar os dados dos estudantes
        student_data = {}

        # Processar cada linha do arquivo
        for line in lines:
            # Remover espaços em branco e quebras de linha
            line = line.strip()

            # Dividir a linha em partes
            parts = line.split()

            # Verificar se a linha possui a estrutura correta
            if len(parts) != 3:
                raise BadLine(f"Linha inválida: {line}")

            first_name, last_name, points_str = parts

            # Converter a pontuação para um número de ponto flutuante
            try:
                points = float(points_str)
            except ValueError:
                raise BadLine(f"Linha inválida: {line}")

            # Atualizar a soma dos pontos do estudante
            full_name = f"{first_name} {last_name}"
            student_data[full_name] = student_data.get(full_name, 0) + points

        # Ordenar o dicionário de dados dos estudantes por ordem alfabética dos nomes
        sorted_data = sorted(student_data.items(), key=lambda x: x[0])

        # Imprimir o relatório
        for name, total_points in sorted_data:
            print(f"{name}\t {total_points}")

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except FileEmpty as e:
        print(e)
    except BadLine as e:
        print(e)


# Solicitar o nome do arquivo ao usuário
filename = input("Digite o nome do arquivo do Prof. Jekyll: ")

# Processar os dados dos estudantes
process_student_data(filename)