frase = str(input('Digite algo: ')).upper().strip()
corta = frase.split()
junta = ''.join(corta)
inverso = junta[::-1]
print(junta, inverso)
if junta == inverso:
    print('{} é um palíndromo'.format(junta))
else:
    print('{} NÃO é um palíndromo'. format(junta))
