# Bytearrays: continuação
#
# Os bytearrays assemelham-se a listas em muitos aspetos. Por exemplo, são mutáveis, são um assunto da função len() , e pode aceder a qualquer um dos seus elementos utilizando a indexação convencional.
#
# Existe uma limitação importante - não deve definir nenhum elemento de byte array com um valor que não seja um número inteiro (violar esta regra causará uma exceção TypeError ) e não lhe é permitido atribuir # um valor que não venha do intervalo 0 a 255 inclusive (a menos que queira provocar uma ValueError exceção).
#
# Pode tratar qualquer elemento do byte array como valores inteiros - tal como no exemplo do editor.
#
# Nota: utilizámos dois métodos para iterar os byte arrays, e fizemos uso da função hex() para ver os elementos impressos como valores hexadecimais.
#
# Agora vamos mostrar-lhe como escrever um byte array num ficheiro binário - binário, pois não queremos guardar a sua representação legível - queremos escrever uma cópia um-para-um do conteúdo da memória 
# física, byte por byte.


data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))