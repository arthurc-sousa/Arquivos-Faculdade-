equipamentos = []
e1 = input("Nome do equipamento 1: ")
equipamentos.append(e1)
e2 = input("Nome do equipamento 2: ")
equipamentos.append(e2)
e3 = input("Nome do equipamento 3: ")
equipamentos.append(e3)
e4 = input("Nome do equipamento 4: ")
equipamentos.append(e4)

urgente = input("Nome do equipamento urgente: ")
equipamentos.insert(0, urgente)
cancelado = input("Nome do equipamento cancelado: ")
if cancelado in equipamentos:
    equipamentos.remove(cancelado)
teste_atual = equipamentos.pop(0)

print("Equipamento que começou a ser testado:", teste_atual)
print("Lista restante:", equipamentos)