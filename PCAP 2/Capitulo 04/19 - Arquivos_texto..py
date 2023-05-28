# Processamento de ficheiros de texto
#
# Nesta lição vamos preparar um ficheiro de texto simples com algum conteúdo curto e simples.
#
# Vamos mostrar-lhe algumas técnicas básicas que pode utilizar para ler o conteúdo do ficheiro, a fim de o processar.
#
# O processamento será muito simples - vai copiar o conteúdo do ficheiro para a consola, e contar todos os carateres que o programa tenha lido.
#
# Mas lembre-se - a nossa compreensão de um ficheiro de texto é muito rigorosa. No nosso sentido, é um ficheiro de texto simples - pode conter apenas texto, sem quaisquer decorações adicionais (formatação, 
# tipos de letra diferentes, etc.).
#
# É por isso que deve evitar criar o ficheiro utilizando qualquer processador de texto avançado como MS Word, LibreOffice Writer, ou algo do género. Utilize os básicos que o seu sistema operativo oferece: 
# Bloco de notas, vim, gedit, etc.
#
# Se os seus ficheiros de texto contiverem alguns carateres nacionais não abrangidos pelo padrão de carateres ASCII, poderá necessitar de um passo adicional. A sua invocação de função open() pode exigir um 
# argumento que denote uma codificação de texto específica.
#
# Por exemplo, se estiver a usar um SO Unix/Linux configurado para usar o UTF-8 como uma configuração de todo o sistema, a função open() pode ter o seguinte aspeto:
# stream = open('file.txt', 'rt', encoding='utf-8')
#
#
# onde o argumento de codificação tem de ser definido para um valor que é uma string que representa a codificação de texto adequada (UTF-8, aqui).
#
# Consulte a documentação do seu SO para encontrar um nome codificador adequado ao seu ambiente.
#
# Nota
#
# Para os fins das nossas experiências com processamento de ficheiros realizadas nesta secção, vamos utilizar um conjunto de ficheiros pré-carregados (ou seja, ficheiros tzop.txt, ou text.txt ) com os quais 
# poderá trabalhar. Se desejar trabalhar com os seus próprios ficheiros localmente na sua máquina, encorajamo-lo vivamente a fazê-lo, e a utilizar o IDLE (ou qualquer outro IDE que possa preferir) para 
# realizar os seus próprios testes.

# Opening tzop.txt in read mode, returning it as a file object:
stream = open("18-tzop.txt", "rt", encoding = "utf-8")

print(stream.read()) # printing the content of the file