import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!', end=' ')
for festa in range(5):
    print(emoji.emojize(':tada: ', use_aliases=True), end='')
    sleep(0.1)
    print(emoji.emojize(':confetti_ball: ', use_aliases=True), end='')
    sleep(0.1)
    print(emoji.emojize(':balloon: ', use_aliases=True), end='')
    sleep(0.1)
