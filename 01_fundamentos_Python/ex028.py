from random import randint
from time import sleep
num = randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um número de 0 a 5, tente adivinhar: ')
print('-=-' * 20)
adv = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if num == adv:
    print('Eu pensei no número: {}. Parabéns, você acertou!!!'.format(num))
else:
    print('Você errou, eu pensei no número: {}'.format(num))
