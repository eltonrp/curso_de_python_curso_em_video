from datetime import date
ano = int(input('Em que ano você nasceu? '))
agora = date.today().year
idade = agora - ano
print('Quem nasceu em {} tem {} anos no ano de {}'.format(ano, idade, agora))
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    alist = agora + saldo
    print('Você deve se alistar daqui a {} ano(s)'.format(saldo))
    print('Você deve se alistar em {}'.format(alist))
else:
    saldo = idade - 18
    alist = agora - saldo
    print('Seu tempo de alistamento já foi há {} ano(s)'.format(saldo))
    print('Seu alistamento foi em {}'.format(alist))
