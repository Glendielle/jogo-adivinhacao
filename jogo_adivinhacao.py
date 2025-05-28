import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        palpite = input("Digite um número entre 1 e 100: ")
        
        if not palpite.isdigit():
            print("Por favor, digite um número válido.")
            continue
        
        palpite = int(palpite)
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

if __name__ == "__main__":
    jogo_adivinhacao()
