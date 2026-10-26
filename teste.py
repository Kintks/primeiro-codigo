ten = int(input("Digite um numero: "))
numero_secreto = 10
contador = 0
chance = 3
while chance > 0:
    if ten == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif ten != numero_secreto:
        chance -= 1
        print("Você errou!, Possui " + str(chance) + " chances restantes. Tente novamente!")
        if chance > 0:
            ten = int(input("Digite um numero: "))
        else:
            print("Suas chances acabaram!")
    else:
        print("Tente novamente!")
