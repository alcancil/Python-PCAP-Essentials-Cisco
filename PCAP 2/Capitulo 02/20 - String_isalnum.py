# Os loops isalnum() .
#
# O método sem parâmetros chamado isalnum() verifica se a string contém apenas dígitos ou carateres alfabéticos (letras) e devolve True ou False de acordo com o resultado.
#
# Veja o exemplo no editor e execute-o.
#
# Nota: qualquer elemento de string que não seja um dígito ou uma letra faz com que o método devolva False. Uma string vazia também o faz.
#

print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


# O output do exemplo é:
# True
# True
# True
# False
# False
# False
#
# output
# 
# Três exemplos mais intrigantes estão aqui:

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())


# Execute-os e verifique o seu output.
# 
# Dica: a causa do primeiro resultado é um espaço - não é nem um dígito nem uma letra.