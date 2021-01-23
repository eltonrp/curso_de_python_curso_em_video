print('{:=^40}'.format(' LOJAS DO POVÃO '))
preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Insira a forma de pagamento: '))
if opção == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        final = preço * 1.2
        juros = preço * 0.2
        print('''Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f}, COM JUROS de 20% (R$ {:.2f})
Valor final será de R$ {:.2f}'''.format(preço, parcela, final / parcela, juros, final))
    else:
        print('Opção incorreta, tente novamente!!')
elif opção == 3:
    parcela = 2
    print('Sua compra de R$ {:.2f} será parcelada em {}x de R$ {:.2f}, SEM JUROS.'.format(preço, parcela, preço/parcela))
elif opção == 1:
    final = preço * 0.9
    desconto = preço * 0.1
    print('''Sua compra será à vista no dinheiro/cheque. 
Sua compra de R$ {:.2f} terá um desconto de 10% (R$ {:.2f}) e será no valor de R$ {:.2f}'''.format(preço, desconto, final))
elif opção == 2:
    final = preço * 0.95
    desconto = preço * 0.05
    print('''Sua compra será à vista no cartão.
Sua compra de R$ {:.2f} terá um desconto de 5% (R$ {:.2f}) e será no valor de R$ {:.2f}'''.format(preço, desconto, final))
else:
    print('Opção incorreta, tente novamente!!')
