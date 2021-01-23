p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))
média = (p1 + p2) / 2
print('Você tirou {:.1f} e {:.1f}. Sua média é {:.1f}'.format(p1, p2, média))
if média < 5:
    print('Está REPROVADO')
elif 7 > média >= 5:
    print('Está de RECUPERAÇÃO')
else:
    print('Está APROVADO')
