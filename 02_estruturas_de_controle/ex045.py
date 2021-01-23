from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('\033[30m{:=^40}'.format(' GAME JOKENPO '))
print('''\033[36mVeja as opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
sleep(1)
jogador = int(input('\033[30mFaça sua escolha: '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[31mJogada INVÁLIDA, tente novamente')
else:
    print('\033[32mJO')
    sleep(1)
    print('\033[34mKEN')
    sleep(1)
    print('\033[35mPO!!!')
    sleep(1)
    print('\033[33m-=' * 11)
    print('Jogador jogou {}'.format(itens[jogador]))
    print('Computador jogou {}'.format(itens[computador]))
    print('-=' * 11)
    if computador == 0:     # computador escolheu PEDRA
        if jogador == 0:
            print('Deu EMPATE!!')
        elif jogador == 1:
            print('Você VENCEU')
        else:
            print('Você PERDEU!!')
    elif computador == 1:     # computador escolheu PAPEL
        if jogador == 0:
            print('Você PERDEU!!')
        elif jogador == 1:
            print('Deu EMPATE!!')
        else:
            print('Você VENCEU!!')
    else:                   # computador escolheu TESOURA
        if jogador == 0:
            print('Você VENCEU!!')
        elif jogador == 1:
            print('Você PERDEU!!')
        else:
            print('Deu EMPATE!!')
