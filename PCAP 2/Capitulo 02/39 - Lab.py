# LAB
#
# Tempo estimado
#
# 30 minutos
# Nível de dificuldade
#
# Médio
# Objetivos
#
#    melhorar as habilidades do aluno a operar com strings;
#    usar strings para representar dados non-text (não-texto).
#
# Cenário
#
# Certamente já viu um display de sete segmentos.
#
# É um dispositivo (por vezes eletrónico, por vezes mecânico) concebido para apresentar um dígito decimal utilizando um subconjunto de sete segmentos. Se ainda não sabe o que é, consulte o seguinte artigo 
# da Wikipédia.
#
# A sua tarefa é a de escrever um programa que seja capaz de simular o trabalho de um dispositivo de seven-display, embora vá utilizar LEDs individuais em vez de segmentos.
#
# Cada dígito é construído a partir de 13 LEDs (uns iluminados, outros escuros, é claro) - é assim que o imaginamos:
#   # ### ### # # ### ### ### ### ### ### 
#   #   #   # # # #   #     # # # # # # # 
#   # ### ### ### ### ###   # ### ### # # 
#   # #     #   #   # # #   # # #   # # # 
#   # ### ###   # ### ###   # ### ### ###
#
# Nota: o número 8 mostra todas as luzes LED acesas.
#
# O seu código tem de fazer um display de qualquer número inteiro não negativo inserido pelo utilizador.
#
# Dica: usar uma lista contendo padrões de todos os dez dígitos pode ser muito útil.
# Dados de teste
# 
# Input de amostra:
# 123
# 
# Exemplo de output:
#  # ### ### 
#  #   #   # 
#  # ### ### 
#  # #     # 
#  # ### ### 
#
# Input de amostra:
# 9081726354
#
# Exemplo de output:
### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 


digitos = [
    ['###', '# #', '# #', '# #', '###'],  # 0
    ['  #', '  #', '  #', '  #', '  #'],  # 1
    ['###', '  #', '###', '#  ', '###'],  # 2
    ['###', '  #', '###', '  #', '###'],  # 3
    ['# #', '# #', '###', '  #', '  #'],  # 4
    ['###', '#  ', '###', '  #', '###'],  # 5
    ['###', '#  ', '###', '# #', '###'],  # 6
    ['###', '  #', '  #', '  #', '  #'],  # 7
    ['###', '# #', '###', '# #', '###'],  # 8
    ['###', '# #', '###', '  #', '###'],  # 9
]

entrada = input("Digite um número: ")
for linha in range(5):
    for digito in entrada:
        print(digitos[int(digito)][linha], end=' ')
    print()

