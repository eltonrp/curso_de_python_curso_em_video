def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: Valor do fatorial de n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(c, end=' = ')
        f *= c
    return f


num = int(input('Número a fazer fatorial: '))
print(fatorial(num, show=True))
help(fatorial)
