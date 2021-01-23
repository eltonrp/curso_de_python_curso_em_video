p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
