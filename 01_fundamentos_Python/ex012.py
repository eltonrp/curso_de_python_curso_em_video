p = float(input('Qual o preço do produto? R$ '))
d = float(1-0.05)
print('Parabéns, você ganhou um desconto de 5% e vai pagar R$ {:.2f}!'
      .format(p*d))
