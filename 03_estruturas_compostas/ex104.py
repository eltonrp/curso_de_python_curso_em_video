def leiaInt(msg):
    a = str(input(msg)).strip()
    while not a.isnumeric():
        print('\033[:31mERRO! Digite um número inteiro válido...\033[:m')
        a = str(input(msg)).strip()
    return int(a)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
