import random

def jogo_forca():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'aprendizado']
    palavra = random.choice(palavras).lower()
    letras_certas = []
    tentativas = 6

    while tentativas > 0:
        for letra in palavra:
            if letra in letras_certas:
                print(letra, end=" ")
            else:
                print("_", end=" ")

        palpite = input("\nDigite uma letra: ").lower()

        if palpite in palavra:
            letras_certas.append(palpite)
            if set(palavra) == set(letras_certas):
                print("Parabéns! Você acertou a palavra!")
                break
        else:
            tentativas -= 1
            print("Letra incorreta! Tentativas restantes:", tentativas)

    if tentativas == 0:
        print("Você perdeu! A palavra correta era:", palavra)

# Exemplo de uso do jogo da forca
jogo_forca()
