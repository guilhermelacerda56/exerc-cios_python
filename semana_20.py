#contador = 1
#while contador <=10:
    #print (contador)
    #contador = contador+1

#condicao = False
#while True:
        #print ("este bloco sempre sera executado pelo menos uma vez. ")
        #if not condicao:
            #break
        #outras operações


        # While tradicional pode não executar se 'condicao' for False
#while condicao:
     # Bloco de código

# Do-While emulado sempre executa pelo menos uma vez
 #while True:
    # Bloco de código
    #if not condicao:
        #break 

while True:
    escolha = input("Escolha uma opção (1, 2, ou 3): ")
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break

