print("Estou estudando Git neste momento!")

name = input("Qual é o seu nome: ")
primeiraNota = float(input("Digite a primeira nota da prova: "))
segundaNota = float(input("Digite a segunda nota da prova: "))
terceiraNota = float(input("Digite a terceira nota da prova: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

print(f"{name} suas notas foram\nNota 1: {primeiraNota}\nNota 2: {segundaNota}\nNota 3: {terceiraNota}\nMédia: {media:.2f}")