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

#O número que sera adivinhado é a variavel numero_secreto, é so mudar o valor para o numero de deseja.
#Obs: é o meu primeiro codigo, se tiver algum erro, ou algo que possa melhorar, sera bem vindo um comentario.
