from curso_em_video.ex109 import moeda

num = float(input('Digite um preço R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'Aumentando {moeda.moeda(num)} em 10% temos {moeda.aumentar(num)}')
print(f'Diminuindo {moeda.moeda(num)} em 13% temos {moeda.diminuir(num, q=13)}')
