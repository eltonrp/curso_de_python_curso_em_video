from curso_em_video.ex108 import moeda

num = float(input('Digite um preço R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando {moeda.moeda(num)} em 10% temos {moeda.moeda(moeda.aumentar(num))}')
print(f'Diminuindo {moeda.moeda(num)} em 10% temos {moeda.moeda(moeda.diminuir(num))}')
