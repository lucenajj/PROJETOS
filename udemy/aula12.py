# texto = int(input('Digite um número: '))
texto = ''
VOGAIS = 'AEIOU'

# Exemplo utilizado um Iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')    

# Exemplo utilizado um Range 
for numero in range(0, 51, 5):
    print(numero, end='')