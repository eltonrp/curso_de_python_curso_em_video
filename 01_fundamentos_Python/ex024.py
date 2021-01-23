cidade = str(input('Qual cidade você nasceu? ')).strip()
separa = cidade.split()
print(separa[0].capitalize() == 'Santo')
print(cidade[:5].upper() == 'SANTO')
