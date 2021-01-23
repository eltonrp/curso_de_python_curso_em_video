matriz = [[], [], []]
somap = somat = maior = 0
for l in range(3):
    for c in range(3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            somat += matriz[l][2]
        if matriz[1][c] > maior:
            maior = matriz[1][c]
    print()
print(f'A soma dos nº pares foi {somap}')
print(f'A soma da 3ª coluna é {somat}')
print(f'O maior valor da segunda linha foi {maior}')
