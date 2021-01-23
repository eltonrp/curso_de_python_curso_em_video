def notas(*n, sit=False):
    """
    -> Recebe vária notas para criar um dicionário
    :param n: Deve informar as notas
    :param sit: Opcional. Informa ou não a situação. False padrão
    :return: Retorna dicionário com a quantidade de notas,
    a maior, menor, média e situação dos alunos
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] < 5:
            r['situação'] = 'PÉSSIMA'
        elif 7 > r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'BOA'
    return r


n = notas(5.5, 2.5, 1.5, sit=True)
print(n)
help(notas)
