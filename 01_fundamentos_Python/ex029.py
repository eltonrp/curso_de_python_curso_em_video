v = float(input('\033[34mDigite a velocidade do carro: '))
if v > 80:
    print('\33[1:31mMULTADO!! Você excedeu o limite de 80 km/h\33[m')
    multa = float((v - 80) * 7.00)
    print('\33[4:33mVocê deve pagar uma multa de R$ {:.2f}\33[m'.format(multa))
print('\33[7mTenha um bom dia. Dirija com segurança!\33[m')
