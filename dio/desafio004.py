menu = '''
[d] Depósitar
[s] Sacar
[e] Extrato
[q] Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)
        
    if opcao == 'd':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito no valor de: R${valor:.2f}\n"
            print (f"\nA sua conta agora possui um saldo total de R$ {saldo:.2f}")
            
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        valor = int(input("\nDigite o valor que você quer sacar:"))
        
        excedeu_saque = numero_de_saques >= LIMITE_DE_SAQUES

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        if excedeu_saldo:
            print('\nSaldo insuficiente para realizar esta transação!')

        if excedeu_saque:
            print ("O limite de saque é 3 por dia e você já realizou os 3 saques diários.")

        if excedeu_limite:
            print ("Valor solicitado ultrapassa seu limite permitido.")
            
        elif valor > 0:
            saldo -= valor
            extrato +=f'Saque no valor de :R${valor:.2f}\n'
            numero_de_saques += 1




        
        if numero_de_saques > 3:
            print('Limite de saques foi atingido')
        

    elif opcao == 'e':

        print(f'Extrato:\nFoi efetuado {numero_de_saques} saques\nSeu limite é de R$ {limite}')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')