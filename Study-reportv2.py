print ()
print ("==== BEM VINDO(A) AO SEU RELATÓRIO SEMANAL DE ESTUDOS ====")
print ()
id_usuario = input("Digite seu nome: ")
horas = float(input("Quantas horas estudou?: "))
materia = input("Qual a materia estudou?: ")
pausa = float(input("Quanto tempo em pausa?: "))

print ("Muito bem!", id_usuario,"agora vamos ao seu relatório oficial!!:\n")

print ("===== STUDY REPORT =====\n")

print ("Nome:", id_usuario)
print ("Horas estudadas:", horas)
print ("Pausa:", pausa)

tempo_produtivo = horas - pausa
produtividade = tempo_produtivo / horas
print() 
print ("Tempo produtivo:", tempo_produtivo)
if tempo_produtivo >= 5:
    print("Nice demais! <3")
elif tempo_produtivo >= 2:
    print ("Está indo muito bem")
else:
    print("precisa focar mais")