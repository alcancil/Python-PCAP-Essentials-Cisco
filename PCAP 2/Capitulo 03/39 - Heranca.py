# Herança - porquê e como?
#
# Antes de começarmos a falar sobre heranças, queremos apresentar um novo e prático mecanismo utilizado pelas classes e objetos Python - a forma como o objeto é capaz de se introduzir a si próprio.
#
# Vamos começar com um exemplo. Veja o código no editor.
#
# O programa imprime apenas uma linha de texto, que no nosso caso é a seguinte:
# <__main__.Star object at 0x7f1074cc7c50>
#
# output
#
# Se executar o mesmo código no seu computador, verá algo muito semelhante, embora o número hexadecimal (a substring a começar por 0x) será diferente, uma vez que é apenas um identificador de objeto interno 
# utilizado pelo Python, e é improvável que pareça o mesmo quando o mesmo código é executado num ambiente diferente.
#
# Como pode ver, a impressão aqui não é realmente útil, e algo mais específico, ou apenas mais bonito, pode ser mais preferível.
#
# Felizmente, o Python oferece precisamente tal função

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun)
