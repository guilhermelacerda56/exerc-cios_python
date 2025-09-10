import random 

numero = random.randint(1,5)

tentativa = 0

while tentativa < 5:
    palpite = int (input("digite o seu palpite de 1 até 5:   "))
    tentativa +=1

    if palpite == numero:
        print ("você acertou o número!")
        break
    elif palpite < numero:
        print ("o número é maior")
    else:
        print("o número é menor")

if palpite != numero:
     print (f"Fim de jogo! O número era {numero}")