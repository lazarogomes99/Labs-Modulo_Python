minhaString = "Olá, meu tipo é String"
print(minhaString)
print(type(minhaString))

# Concatenando strings
print("\n--- Concatenando Strings ---\n")
primeiraString = "Cacho"
segundaString = "eira"
terceiraString = primeiraString + segundaString
print(terceiraString)

# Strings de entrada
print("\n--- Strings de entrada ---\n")
name = input("Qual o seu nome? \n")
print(f"Seu nome é {name}")


# Formatação de Strings de Saída
cor = input("Qual sua cor favorita? \n")
animal = input("Qual seu animal favorito?\n ")
print(f"{name}, você adora a cor {cor} e seu animal preferido é {animal}!")