# if é uma palavra-chave que inicia uma estrutura condicional, permitindo que o código execute um bloco de instruções apenas se uma determinada condição for verdadeira 

# elif  Verifica uma condição alternativa, se a condição do if for falsa. Vários

#else Executa um bloco de código se nenhuma das condições anteriores for verdadeira. 

# calculo de multiplicação operação matemática que combina dois ou mais valores para produzir um resultado

quantidade_desejada = int(input('Digite a quantidade do produto desejada: '))

if quantidade_desejada >= 10:
    print('Produto disponível em estoque. Aproveite!')
else:
    print('Produto indisponível no momento. Volte mais tarde!')
