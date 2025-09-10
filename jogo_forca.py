palavra = "alice"

acertos = []

erros = 0

while erros < 3 and len (acertos) < len (set(palavra)):
    letra = input ("digite uma letra  ")

    if letra in palavra:
        if letra not in acertos:
            acertos.append (letra)
        print ("letra correta")    
    else:
        erros +=1
        print(f"letra incorreta! você tem {3-erros} tentativas")   
if len (acertos) == len (set(palavra)):
    print ("parabéns! você acertou a palavra")
else:
     print (f"Fim de jogo! A palavra era: {palavra}")        
        
