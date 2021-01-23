sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Informe o sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} informado, registrado com sucesso!'.format(sexo))
