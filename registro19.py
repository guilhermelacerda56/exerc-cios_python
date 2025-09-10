N = int(input("digite um numero inteiro:"))

for i in range(1,N+1):
    print(f"{i} {i**2} {i**3}")
    print(f"{i} {i**2 + 1} {i**3 + 1}")

    #input → recebe dados digitados pelo usuário.
#int → converte um valor para número inteiro.
#for → repete um bloco de código várias vezes.
#range → gera uma sequência de números para ser usada no loop.
#i → é uma variável que representa cada valor da sequência dentro do loop.
#in → indica que o loop vai percorrer (iterar) os valores de uma sequência, como a gerada por range().


