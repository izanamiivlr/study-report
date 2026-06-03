print("Calculadora de Descanso\n")
id_usuario = input("Qual seu nome?: ")
horas_dormidas = float(input("Quantas horas você dormiu?: "))
horas_acordada = float(input("Quantas horas ficou acordada?: "))
print()

print("Olá", id_usuario)
print("segue abaixo seu resultado:\n ")
print("Horas dormidas:", horas_dormidas)
print("Horas acordada:", horas_acordada)
if horas_dormidas >= 8:
    print("Dormiu muito bem!")
    if horas_dormidas >= 10:
        print("Caraca, tá recuperando até o sono da semana passada")
elif horas_dormidas >= 5:
    print("cuidado, sono é importante")
else:
    print("Cara, ta na hora de regular esse sono ai")
