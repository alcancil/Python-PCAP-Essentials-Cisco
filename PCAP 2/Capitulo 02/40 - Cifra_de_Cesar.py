# A Cifra César: encriptar uma mensagem
#
# Vamos mostrar-lhe quatro programas simples, para apresentar alguns aspetos do processamento de string em Python. Eles são propositadamente simples, mas os problemas do lab serão significativamente mais 
# complicados.
#
# O primeiro problema que queremos mostrar chama-se Caesar cipher - mais detalhes aqui: https://en.wikipedia.org/wiki/Caesar_cipher.
#
# Esta cifra foi (provavelmente) inventada e usada por Caio Júlio César e suas tropas durante as Guerras Gálicas. A ideia é bastante simples - cada letra da mensagem é substituída pela sua consequente mais 
# próxima (A torna-se B, B torna-se C, e assim por diante). A única exceção é Z, que se torna A.
#
# O programa no editor é uma implementação muito simples (mas funcional) do algoritmo.
#
# Escrevemo-lo utilizando os seguintes pressupostos:
#
#     aceita apenas letras latinas (nota: os romanos não usavam espaços em branco nem dígitos)
#     todas as letras da mensagem estão em maiúsculas (nota: os romanos conheciam apenas maiúsculas)
#
# Vamos rastrear o código:
#
#     linha 02: pedir ao utilizador para inserir a mensagem aberta (não encriptada), de uma linha;
#     linha 03: preparar uma string para uma mensagem encriptada (vazia por agora)
#     linha 04: iniciar a iteração através da mensagem;
#     linha 05: se o caratere atual não for alfabético...
#     linha 06: ...ignorá-lo;
#     linha 07: converter a letra em maiúsculas (é preferível fazê-lo cegamente, em vez de verificar se é necessário ou não)
#     linha 08: obter o código da letra e incrementá-lo em um;
#     linha 09: se o código resultante tiver “deixado” o alfabeto latino (se for maior do que o código Z)...
#     linha 10: ...alterá-lo para o código A;
#     linha 11: anexar o caratere recebido ao fim da mensagem encriptada;
#     linha 13: imprimir a cifra.
#
# O código, alimentado com esta mensagem:
# AVE CAESAR
# 
# tem como output:
# BWFDBFTBS
# 
# output
#
# Faça os seus próprios testes.

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)