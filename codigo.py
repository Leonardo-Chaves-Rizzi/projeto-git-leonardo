while True:
    nome = input("Qual é o seu nome: ")

    if nome.isalpha():
        break
    else:
        print("O nome deve conter apenas letras!")

print("-" * 15)
print(f"Olá {nome}!")
print("-" * 15)

while True:
    primeiraNota = float(input("Digite a primeira nota da prova: "))
    segundaNota = float(input("Digite a segunda nota da prova: "))
    terceiraNota = float(input("Digite a terceira nota da prova: "))

    media = (primeiraNota + segundaNota + terceiraNota) / 3

    if primeiraNota > 10 or segundaNota > 10 or terceiraNota > 10:
        print("Digite novamente as notas!")
        continue
    else:
        if media >= 6:
            situacao = "aprovado"
            break

        else:
            situacao = "reprovado"
            break

print(f"{nome} suas notas foram\nNota 1: {primeiraNota}\nNota 2: {segundaNota}\nNota 3: {terceiraNota}\nMédia: {media:.2f}\nDe acordo com sua média, você está {situacao}!")