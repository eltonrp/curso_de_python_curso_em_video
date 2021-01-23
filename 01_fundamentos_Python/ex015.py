dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km rodados com o carro: '))
diaria = float(dias * 60)
kmrod = float(km * 0.15)
aluguel = diaria + kmrod
print('Considerando a quilometragem rodada de {} km '
      'e um total de {} dias,\no valor do aluguel é de R$ {:.2f}'
      .format(km, dias, aluguel))
