def escreva():
    msg = str(input('Escreva uma msg: '))
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)


escreva()
