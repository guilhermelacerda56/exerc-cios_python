# input é uma função que permite que o programa receba dados inseridos pelo usuário através do terminal.

# calculo de divisão e uma  operação matemática que divide um número (o dividendo) por outro (o divisor) para obter o quociente.

numero = int(input('Digite um número: '))

if numero > 0:
    print('O número digitado e positivo!')
elif numero < 0:
    print('O número digitado e  negativo.')
else:
    print('O número digitado é zero.')
