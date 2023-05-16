# O validador IBAN
#
# O quarto programa implementa (de uma forma ligeiramente simplificada) um algoritmo utilizado pelos bancos europeus para especificar números de conta. A norma denominada IBAN (International Bank Account 
# Number) fornece um método simples e bastante fiável de validação dos números de conta contra erros de digitação simples que possam ocorrer durante a reescrita do número, por exemplo, de documentos em 
# papel, como faturas ou contas, para computadores.
#
# Pode encontrar mais detalhes aqui: https://en.wikipedia.org/wiki/International_Bank_Account_Number.
#
#Um número de conta compatível com IBAN consiste em:
#
#    um código de país de duas letras retirado da norma ISO 3166-1 (por exemplo, FR para a França, GB para a Grã-Bretanha, DE para a Alemanha, e assim por diante)
#    dois dígitos de verificação utilizados para realizar as verificações de validade - testes rápidos e simples, mas não totalmente fiáveis, mostrando se um número é inválido (distorcido por uma gralha) ou # se parece ser válido;
#     o número real da conta (até 30 carateres alfanuméricos - o comprimento desta parte depende do país)
#
# A norma diz que a validação requer os seguintes passos (de acordo com a Wikipédia):
#
#     (passo 1) Verificar se o comprimento total do IBAN está correto de acordo com o país (este programa não o fará, mas pode modificar o código para cumprir este requisito, assim o desejar; nota: tem de 
# ensinar ao código todos os comprimentos utilizados na Europa)
#    (passo 2) Mover os quatro carateres iniciais para o final da string (ou seja, o código do país e os dígitos de verificação)
#    (passo 3) Substituir cada letra na string por dois dígitos, expandindo assim a string, onde A = 10, B = 11... Z = 35;
#    (passo 4) Interpretar a string como um número inteiro decimal e calcular o resto desse número na divisão por 97; Se o resto for 1, o teste de verificação de dígito é passado e o IBAN pode ser válido.
#
# Veja o código no editor. Vamos analisá-lo:
#
#    linha 03: pedir ao utilizador para introduzir o IBAN (o número pode conter espaços, uma vez que melhoram significativamente a legibilidade do número...
#    linha 04: ...mas remova-os imediatamente)
#    linha 05: o IBAN inserido deve consistir apenas em dígitos e letras - se não consistir...
#    linha 06:... fazer output da mensagem;
#    linha 07: o IBAN não deve ser menor do que 15 carateres (esta é a variante mais curta, usada na Noruega)
#    linha 08: se for mais curto, o utilizador é informado;
#    linha 09: além disso, o IBAN não pode ter mais de 31 carateres (esta é a variante mais longa, usada em Malta)
#    linha 10: se for mais longo, fazer um aviso;
#    linha 11: iniciar o processamento em si;
#    linha 12: mover os quatro carateres iniciais para o final do número e converter todas as letras em maiúsculas (passo 02 do algoritmo)
#    linha 13: esta é a variável utilizada para completar o número, criada através da substituição das letras por dígitos (de acordo com o passo 03 do algoritmo)
#    linha 14: iterar através do IBAN;
#    linha 15: se o caratere é um dígito...
#    linha 16: basta copiá-lo;
#    linha 17: caso contrário...
#    linha 18: ...convertê-lo em dois dígitos (observe como tal é feito aqui)
#    linha 19: a forma convertida do IBAN está pronta - fazer um inteiro dele;
#    linha 20: é o resto da divisão de iban2 por 97 igual a 1?
#    linha 21: Se sim, então sucesso;
#    linha 22: Caso contrário...
#    linha 23: ...o número é inválido.
#
# Vamos adicionar alguns dados de teste (todos estes números são válidos - pode invalidá-los alterando qualquer caratere).
#
#    Britânico: GB72 HBZU 7006 7212 1253 00
#    Francês: FR76 30003 03620 00020216907 50
#    Alemão: DE02100100100152517108
#
# Se for um residente da UE, pode usar o seu próprio número de conta para testes.

# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")