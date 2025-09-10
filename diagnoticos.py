

febre = input("Você está com febre? ")
dor_corpo = input("Você sente dores no corpo? ")
coriza = input("Você está com coriza (nariz escorrendo)? ")
espirros = input("Você está espirrando? ")

if febre == "sim":
        if dor_corpo == "sim":
            print("Diagnóstico: Pode ser gripe.")
        else:
            print("Diagnóstico: Pode ser um resfriado.")
else:
        if espirros == "sim" and coriza == "sim":
            print("Diagnóstico: Pode ser uma alergia.")
        elif coriza == "sim":
            print("Diagnóstico: Pode ser um resfriado leve.")
        else:
            print("Diagnóstico: Sem indícios claros de doença. Procure um médico se persistirem os sintomas.")


