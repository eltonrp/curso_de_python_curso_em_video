peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / (altura**2)
print('Seu imc é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Parabéns, você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc <=40:
    print('Você está na faixa de Obesidade')
else:
    print('Você está com obesidade mórbida, cuidado!')
