# Mais sobre exceções
#
# Discutir a programação de objetos oferece uma excelente oportunidade para regressar às exceções. A natureza objetiva das exceções de Python torna-as uma ferramenta muito flexível, capaz de se adaptar a 
# necessidades específicas, mesmo aquelas que ainda não conhece.
#
# Antes de mergulharmos na face objetiva das exceções, queremos mostrar-lhe alguns aspetos sintáticos e semânticos da forma como o Python trata o bloco try-except, uma vez que oferece um pouco mais do que 
# aquilo que temos apresentado até agora.
#
# A primeira característica que queremos discutir aqui é um possível ramo adicional, que pode ser colocado dentro (ou melhor, diretamente atrás) do bloco try-except - é a parte do código que começa com else - # tal como no exemplo no editor.
#
# Um código assim rotulado é executado quando (e apenas quando) nenhuma exceção tiver sido levantada dentro da parte try: . Podemos dizer que exatamente um ramo pode ser executado após try: - quer o que 
# começa com except (não se esqueça de que pode haver mais do que um ramo deste tipo) ou o que começa com else.
#
# Nota: o ramo else: tem de ser localizado após o último ramo except .
#
# O código de exemplo produz o seguinte output:
# Everything went fine
# 0.5
# Division failed
# None

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        return None
    else:
        print("Everything went fine")
        return n


print(reciprocal(2))
print(reciprocal(0))
