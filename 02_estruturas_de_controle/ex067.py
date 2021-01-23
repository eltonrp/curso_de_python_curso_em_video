while True:
    n = int(input('Qual tabuada quer ver?\n[Um nº negativo para sair] '))
    print('=' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        produto = c * n
        print(f'{n} x {c:2} = {produto}')
    print('=' * 20)
print('{:^20}'.format('Fim do Programa'))
print('=' * 20)
