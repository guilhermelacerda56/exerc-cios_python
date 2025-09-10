severidade = int (input ("digite o nivel da severidade: 1 a 5 "))

probabilidade =int (input (" digite o nivel da propabilidade: 1 a 5 "))

if severidade >3 and probabilidade >3:
    print ("risco de alta prioridade ")
elif severidade >3 or probabilidade >3:
    print (" risco de media prioridade ")
else:
    print (" risco de baixa prioridade ")
    