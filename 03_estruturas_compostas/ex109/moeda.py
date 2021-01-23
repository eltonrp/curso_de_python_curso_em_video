def aumentar(n, q=10, f=True):
    n *= (1 + (q/100))
    '''if f:
        return moeda(n)
    else:
        return n'''
    return moeda(n) if f is True else n


def diminuir(n, q=10, f=True):
    n *= (1 - (q/100))
    return moeda(n) if f is True else n


def dobro(n, f=True):
    n *= 2
    return moeda(n) if f is True else n


def metade(n, f=True):
    n /= 2
    return moeda(n) if f is True else n


def moeda(p=0, moeda='R$'):
    # n = str(f'{n:.2f}')
    # m = n.replace('.', ',')
    return f'{moeda}{p:.2f}'.replace('.', ',')
