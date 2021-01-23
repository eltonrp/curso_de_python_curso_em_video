from datetime import date
ano = int(input('Qual ano deseja avaliar? Colococar 0 para ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} \033[34mé Bissexto'.format(ano))
else:
    print('O ano {} \033[31mNÃO é Bissexto'.format(ano))
