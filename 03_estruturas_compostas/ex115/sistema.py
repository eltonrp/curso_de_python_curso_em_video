from curso_em_video.ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Acessar cadastro', 'Cadastrar novo', 'Descadastrar', 'Sair'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cadastrar(arq)
    elif resposta == 3:
        descadastrar(arq)
    elif resposta == 4:
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
