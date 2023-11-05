import random

print("\n\n-------------------------------------------")
print("------- M I S T E R Y   G A M E -----------")
print("-------------------------------------------\n")
print("As regras são simples, pensarei em um número e você tenta adivinhas.")

numero = random.randint(1,10)
numeroUser = False

while numeroUser != True:
    adivinhar = input("Adivinhe um número de 1 a 10: ")
    if int(adivinhar) == numero:
        print(f"Você digitou {adivinhar}. Está correto, você venceu!")
    else:
        print(f"Você digitou {adivinhar}. Desculpe, está errado. Tente novamente.")

