import random

def imprime_grid(grid) :
    print("O Status do Grid e :\n")
    for indice in range(len(grid)) :
        print(grid[indice], end = " ")
        if indice == 2 or indice == 5 or indice == 8 :
           print(" ")

def verifica_grid(grid, jogador) :
    #Testando as linhas
    if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
   
    # Testando as colunas
    if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    
    # Testando as diagonais
    if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2
    if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador :
       if jogador == "X" :
          return 1
       else:
          return 2 

    return 0 

quantidade_escolhas = 0

print("-" * 100)
print(" " * 30, "Bem vindo ao Jogo da Velha")
print(" " * 25, "Voce vai jogar contra o Computador")
print(" " * 10, "Ganha quem conseguir uma linha, coluna ou diagonal com o mesmo simbolo")
print("-" * 100)

print("Voce precisa escolher uma posicao no grid paracar sua jogada, de acordo com a numeracao, veja o grid")

print("- - -")
print("- - -")
print("- - -")
print ("Escolha um numero de 1 a 9 para sua jogada, conforme o grid a seguir : ")
print("1 2 3")
print("4 5 6")
print("7 8 9")

grid = ["_"] * 9

while True :

      escolha = int(input("Qual e sua escolha ? : "))

      while grid[escolha -1] != "_" :
            print("Essa posicao ja foi escolhida. Escolha outra")
            imprime_grid(grid)
            escolha = int(input("Qual e sua escolha ? : "))

      grid[escolha-1] = "X"
      quantidade_escolhas += 1
      vencedor = verifica_grid(grid,"X")
      if vencedor != 0 :
         break
      if quantidade_escolhas == 9 :
         break
      imprime_grid(grid)

      escolha_pc = random.randint(1,9)

      while grid[escolha_pc - 1] != "_" :
            escolha_pc = random.randint(1,9)
      
      print("A escolha do computador e : ", escolha_pc)
      grid[escolha_pc - 1] = "0"
      quantidade_escolhas += 1
      vencedor = verifica_grid(grid,"0") 
      if vencedor != 0 :
         break
      
      imprime_grid(grid)

if vencedor == 1 :
   print("PARABENS, VOCE GANHOU O JOGO")
elif vencedor == 2 :
   print("VOCE PERDEU")
else:
   print("DEU EMPATE")

imprime_grid(grid)


