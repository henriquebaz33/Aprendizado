velocidade = float(input('Qual a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7

    print('\033[31mMULTADO! Você exedeu o limite permitido que é de 80Km/h\033[m')
    print(f'\033[31mVocê deve pagar uma multa de R${multa:.2f}\033[m')
print('\033[33mTenha um bom dia e dirija com segurança!\033[m')
