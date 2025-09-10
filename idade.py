dias = int (input (" digite a sua idade em dias "))

anos = dias // 365 

dias = dias % 35 

meses = dias // 30 

dias = dias % 30 

print ( f" {anos} anos")

print (f"{ meses} meses")

print ( f" {dias} dias")