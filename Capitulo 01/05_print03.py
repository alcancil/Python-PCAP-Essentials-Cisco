
# A função print() - os carateres de escape e de newline
# Modificámos novamente o código. Olhe com atenção.
# 
# Há duas mudanças muito subtis - inserimos um estranho par de carateres dentro da rima. Têm este aspeto: \n.

# Curiosamente, enquanto se pode ver dois carateres, o Python vê um.
# A barra invertida (\) tem um significado muito especial quando usado dentro de strings - a isto chama-se o caratere de escape.

# A palavra escape deve ser entendida especificamente - significa que a série de carateres na string escapa por um 
# momento (um momento muito curto) para introduzir uma inclusão especial.

# Por outras palavras, a barra invertida não significa nada em si, mas é apenas uma espécie de anúncio de que o próximo caratere 
# após a barra invertida também tem um significado diferente.

# A letra n colocada após a barra invertida vem da palavra newline (nova linha).
# Tanto a barra invertida como o n formam um símbolo especial chamado um caratere de newline, que incita a consola a iniciar 
# uma nova linha de output.

print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")
