from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - nascimento
while True:
    cadastro['CTPS'] = int(input('Carteira de Trabalho (0 = não tem): '))
    if cadastro['CTPS'] == 0:
        break
    if cadastro['CTPS'] > 0:
        cadastro['Ano de Contratação'] = int(input('Ano de contratação: '))
        cadastro['Salário'] = float(input('Salário: '))
        cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (datetime.now().year - cadastro['Ano de Contratação']))
        break
    else:
        print('Dados inválidos, tente novamente...')
if cadastro['CTPS'] == 0:
    cadastro['CTPS'] = 'Não tem CTPS'
print('-' * 30)
for k, v in cadastro.items():
    print(f'   - {k} = {v}')
