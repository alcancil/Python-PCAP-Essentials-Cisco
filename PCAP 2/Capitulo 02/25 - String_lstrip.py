# Os loops lstrip () .
#
# O parâmetro sem lstrip() método devolve uma cadeia recém-criada formada a partir da original, removendo todos os principais espaços em branco.
#
# Analise o código de exemplo no editor.
#
# Os parêntesis não fazem parte do resultado - apenas mostram os limites do resultado.
#
# O output do exemplo:
# [tau ]
#
# output
#
# O parâmetro único lstrip() faz o mesmo que a sua versão sem parâmetros, mas remove todos os caracteres alistados no seu argumento (uma cadeia), e não apenas espaços em branco:
print("www.cisco.com".lstrip("w."))
# 
#
# Não são necessários parêntesis aqui, pois o output é o seguinte:
# cisco.com
#
# output
#
# Consegue adivinhar a saída do trecho abaixo? Pense bem. Execute o código e verifique as suas previsões.
print("pythoninstitute.org".lstrip(".org"))
#
#
# Surpreendido? Carateres principais , espaços em branco principais. Mais uma vez, experimente com os seus próprios exemplos.
#
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
