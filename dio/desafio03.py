n = int(input())  # primeiro número que entra é o '4' que é a quantidade de loops que deve ser feito

while n > 0:
    N = input().split(" ")  # aqui onde o número será inserido e separados numa lista


    A = N[0]  # item com indice 0 da lista
    B = N[1]  # item com indice 1 da lista

    b = -len(B)  # iremos reservar o tamanho do item B

    if (0<len(A)<=1000) and (0<len(B)<=1000): #checaremos se o tamanho dos itens está dentro do permitido

      if len(A) >= len(B):     # checaremos se o tamanho de A é maior que B

          if A[b:] == B:       # iremos comparar se o final de A é igual o número B
              print('encaixa')
          else:
              print('nao encaixa')
      else:
          print('nao encaixa')
      
      n -= 1