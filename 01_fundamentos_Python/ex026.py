frase = str(input('Digite uma frase qualquer: ')).lower().strip()
print('A letra A aparece {} vez(es)'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('a') + 1))
print('A letra A aparece pela última vez na posição: {}'.format(frase.rfind('a') + 1))
