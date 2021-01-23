aluno = {}
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    resultado = 'Aprovado'
else:
    resultado = 'Reprovado'
aluno['resultado'] = resultado
#print(f'O aluno {aluno["nome"]}, teve média {aluno["média"]:.1f} e está {aluno["resultado"]}!!')
for k, v in aluno.items():
    print(f'{k.title()} = {v}' if k != 'média' else f'{k.title()} = {v:.1f}')
