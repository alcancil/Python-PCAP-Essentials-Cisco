# Criar objetos time .
#
# Já sabe como apresentar uma data utilizando o objeto date . O módulo datetime também tem uma classe que lhe permite apresentar o tempo. Consegue adivinhar o seu nome? Sim, é chamada time:
#
# time(hour, minute, second, microsecond, tzinfo, fold)
#
# A função time aceita os seguintes parâmetros opcionais:
# Parâmetro 	Restrições
# hour 	
#
# O parâmetro hora deve ser maior ou igual a 0 e inferior a 23.
# minute 	
#
# O parâmetro minuto deve ser maior ou igual a 0 e inferior a 59.
# second 	
#
# O parâmetro segundo deve ser maior ou igual a 0 e inferior a 59.
# microsecond 	
#
# O parâmetro microssegundo deve ser maior ou igual a 0 e inferior a 1000000.
# tzinfo 	
# 
# O parâmetro tzinfo deve ser um objeto de subclasse tzinfo ou None (default).
# fold 	
#
# O parâmetro fold deve ser 0 ou 1 (padrão 0).
#
# O parâmetro tzinfo está associado a fusos horários, enquanto o fold está associado a tempo de relógio. Não os utilizaremos durante este curso, mas encorajamo-lo a familiarizar-se com eles.

from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
