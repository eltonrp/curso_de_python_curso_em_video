opção = 'S'
cont = soma = maior = menor = 0
while opção == 'S':
    n = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    cont += 1
    soma += n
    opção = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while opção not in 'SN':
        print('Opção inválida, tente novamente...')
        opção = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
média = float(soma / cont)
print('Você digitou {} números e a média foi {:.2f}'.format(cont, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
