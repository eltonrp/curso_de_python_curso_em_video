def aumentar(n, q=10, f=True):
    n *= (1 + (q/100))
    '''if f:
        return moeda(n)
    else:
        return n'''
    return moeda(n) if f else n


def diminuir(n, q=10, f=True):
    n *= (1 - (q/100))
    return moeda(n) if f else n


def dobro(n, f=True):
    n *= 2
    return moeda(n) if f else n


def metade(n, f=True):
    n /= 2
    return moeda(n) if f else n


def moeda(p=0, moeda='R$'):
    # n = str(f'{n:.2f}')
    # m = n.replace('.', ',')
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(preço=0, aum=10, desc=5):
    print('-' * 30)
    # print(f'{"RESUMO DO VALOR":^30}')
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço analisado: ":17}{moeda(preço):>13}')
    print(f'{"Dobro do preço: ":17}{dobro(preço):>13}')
    print(f'{"Metade do preço: ":17}{metade(preço):>13}')
    print(f'{aum:2}{"% de aumento: ":15}{aumentar(preço, aum):>13}')
    print(f'{desc:2}{"% de redução: ":15}{diminuir(preço, desc):>13}')
    print('-' * 30)
