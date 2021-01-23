def aumentar(n, q=10):
    n *= (1 + (q/100))
    return n


def diminuir(n, q=10):
    n *= (1 - (q/100))
    return n


def dobro(n):
    n *= 2
    return n


def metade(n):
    n /= 2
    return n


def moeda(p=0, moeda='R$'):
    #n = str(f'{n:.2f}')
    #m = n.replace('.', ',')
    return f'{moeda}{p:.2f}'.replace('.', ',')
