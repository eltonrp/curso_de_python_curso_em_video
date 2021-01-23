def aumentar(n, q=10):
    n *= (1 + (q/100))
    return f'{n:.2f}'


def diminuir(n, q=10):
    n *= (1 - (q/100))
    return f'{n:.2f}'


def dobro(n):
    n *= 2
    return f'{n:.2f}'


def metade(n):
    n /= 2
    return f'{n:.2f}'
