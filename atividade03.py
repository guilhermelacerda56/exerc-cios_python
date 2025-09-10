# calculo de adição operação de somar dois ou mais valores numéricos para obter um resultado

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 100:
    desconto = float(valor_compra - (valor_compra/10))
    print('valor da compra com desconto e:', desconto)
else:
    print('valor da compra sem desconto:', valor_compra)

  
