expressão = str(input('Digite a expressão: '))
pilha = []
for l in expressão:
    if l == '(':
        pilha.append('(')
    elif l == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('Expressão inválida')
else:
    print('Expressão válida')
