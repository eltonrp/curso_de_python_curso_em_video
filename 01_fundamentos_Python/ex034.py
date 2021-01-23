sal = float(input('Qual o seu salário? R$ '))
if sal <= 1250:
    aumento = sal * 1.15
    print('Você teve um aumento de \033[31m15%\033[m\n'
          'Seu salário agora é de R$ \033[34m{:.2f}'.format(aumento))
else:
    aumento = sal * 1.10
    print('Você teve um aumento de \033[31m10%\033[m\n'
          'Seu salário agora é R$ \033[34m{:.2f}'.format(aumento))
#print('Seu salário agora é R$ {}'.format(aumento))
