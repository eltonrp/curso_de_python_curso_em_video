from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print('O atleta nasceu em {} e tem {} anos'.format(ano, idade))
if idade <= 9:
    print('Atleta da categoria MIRIM')
elif idade <= 14:
    print('Atleta da categoria INFANTIL')
elif idade <= 19:
    print('Atleta da categoria JÚNIOR')
elif idade <= 25:
    print('Atleta da categoria SÊNIOR')
else:
    print('Atleta da categoria MASTER')
