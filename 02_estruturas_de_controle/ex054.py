from datetime import date
atual = date.today().year
maioridade = atual - 21
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Digite o {}° ano de nascimento: '.format(c)))
    if ano <= maioridade:
        maior += 1
    else:
        menor += 1
print('Foram encontrados {} maiores de idade'.format(maior))
print('E {} menores de idade'.format(menor))
