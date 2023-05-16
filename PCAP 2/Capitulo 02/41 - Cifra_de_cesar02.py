# A Cifra César: decifrar uma mensagem
#
# A transformação inversa deve agora ser clara para si - vamos apenas apresentar-lhe o código tal como está, sem quaisquer explicações.
#
# Veja o código no editor. Verifique cuidadosamente se funciona. Use o criptograma do programa anterior.

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)