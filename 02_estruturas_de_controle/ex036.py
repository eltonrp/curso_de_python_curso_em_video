casa = float(input('Qual o valor da casa? R$ '))
salário = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos deseja pagar? '))
parcela = casa / (tempo * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, tempo, parcela))
if parcela / salário <= 0.3:
    print('Parabéns, empréstimo CONCEDIDO!!')
else:
    print('Desculpe, o empréstimo foi NEGADO')
