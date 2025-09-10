cargo = input("Cargo do funcionário: ").lower().strip()
dia = input("Dia da semana: ").lower().strip()

dias_uteis = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

if cargo == "gerente":
    print("Acesso permitido.")
elif cargo in ["analista", "estagiário"] and dia in dias_uteis:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
