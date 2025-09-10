import random
numero = random.randint (1,5)

tentativas =0

while True:

    palpite = int (input("digite um numero de 1 ate 5"))
    tentativas  += 1

    if palpite < numero:
        print(" o numero e o maior")
    elif palpite > numero:
        print("o numero e menor")
    else: 
        print (" voce acertou o numero")
    break