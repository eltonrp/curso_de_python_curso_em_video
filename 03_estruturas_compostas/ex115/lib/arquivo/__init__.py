from curso_em_video.ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            nome = leianome('Nome: ')
            idade = leiaint('Idade: ')
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na escrita dos dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def descadastrar(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um problema na abertura do arquivo')
    else:
        try:
            nome = leianome('Nome a remover: ')
            lista2 = []
            lista = a.readlines()
            a.close()
            for item in lista:
                itemn = item.split(';')
                lista2.append(itemn)
            for pos, item in enumerate(lista2):
                if item[0] == nome:
                    del lista2[pos]
            lista3 = []
            for item in lista2:
                item2 = ';'.join(item)
                lista3.append(item2)
            a = open(arq, 'wt')
            for itens in lista3:
                a.write(itens)
            a.close()
        except:
            print(f'Houve um erro na remoção de {nome}')
        else:
            print(f'{nome} removido com sucesso')
