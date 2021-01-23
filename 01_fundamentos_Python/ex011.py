l = float(input('Dê a largura da parede: '))
h = float(input('Agora a altura: '))
a = l * h
print('A área da parede é de: {:.2f}'.format(a))
print("Para pintar esta parede, será necessário: {:.2f} litros de tinta!"
      .format(a/2))
