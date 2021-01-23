somai = 0
somam = 0
maiorih = 0
nomevelho = ''
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somai += idade
    if c == 1 and sexo in 'Mm':
        maiorih = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorih:
        maiorih = idade
        nomevelho = nome
    if idade < 20  and sexo in 'Ff':
        somam += 1
mediai = somai / 4
print('A média da idade do grupo é de {:.1f} anos.'.format(mediai))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorih, nomevelho))
print('Temos {} mulher(es) menor(es) de 20 anos no grupo.'.format(somam))
