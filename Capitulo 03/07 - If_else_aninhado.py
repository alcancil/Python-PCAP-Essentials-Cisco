# IF ELSE ANINHADO
#
# Pode existir situaçãoes em que queremos testar duas ou mais condiçoes if. Uma dentro da outra. Isso se chama aniunhra uma em outra.
#
# Ex:
n = input("Digite um númemero entre 10 e 20 : ")
if int(n) >= 10:
   if int(n) <= 20:
      n = int(n) + 10
      print(n)
else:       
     print("O numero digitado esta fora do intervalo 10 e 20!!")
     