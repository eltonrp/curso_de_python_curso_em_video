s = float(input('Qual o seu salário? R$ '))
print('Você ganha R$ {:.2f}. Está na hora de ter um aumento!'
      .format(s), end=' ')
print('Parabéns, você teve um aumento de 15%!\n'
      'Seu salário agora é R$ {:.2f}'.format(s*1.15))
