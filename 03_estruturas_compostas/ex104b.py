def leiaInt(msg):
    ok = False
    while True:
        núm = str(input(msg)).strip()
        if núm.isnumeric():
            núm = int(núm)
            ok = True
        else:
            print('\033[:31mERRO! Digite um número inteiro válido...\033[:m')
        if ok:
            break
    return núm


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
