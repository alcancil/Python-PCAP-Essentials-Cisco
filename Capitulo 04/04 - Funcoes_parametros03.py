# Funções parametrizadas: continuação
# Uma função pode ter tantos parâmetros quantos quiser, mas quanto mais parâmetros tiver, mais difícil é memorizar os seus papéis e propósitos.
#
# Funções como o conceito de caixa negra
#
# Vamos modificar a função - tem dois parâmetros agora:
#
# def message(what, number):
#    print("Enter", what, "number", number)
#
#
# Isto também significa que invocar a função irá requerer dois argumentos.
#
# O primeiro parâmetro novo destina-se a levar o nome do valor desejado.
#
# Aqui está:
#
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")



# Esta é o output que está prestes a ver:
#
# Enter telephone number 11
# Enter price number 5
# Enter number number number
# output
#
#
# Execute o código, modifique-o, adicione mais parâmetros e veja como isso afeta o output.

