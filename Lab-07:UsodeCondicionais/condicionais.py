respostaUsuario = input("Você precisa enviar um pacote? (Digite 'sim' ou 'não')\n")

if respostaUsuario == "sim":
    print("Legal, podemos te ajudar a enviar o pacote! c:")
else:
    print("Por favor, volte quando precisar enviar o pacote, obrigado.")

print("-" *50)
# Usando a declaração elif.

segundaResposta = input("Gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Insira selos, envelope ou copia) ")

if segundaResposta == "selos":
    print("Temos muitos designs de carimbos para você escolher.")
elif segundaResposta == "envelope":
    print("Temos vários tamanhos de envelope para escolher.")
elif segundaResposta == "copia":
    copias = input("Quantas cópias você deseja? (Digite um número) ")
    print(f"Aqui estão as {copias} cópias.")
else:
    print("Obrigado, por favor volte novamente.")




    