from time import sleep

nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
sleep(1)

print(f'Seu nome em maiúsulas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')

nome_separado = nome.split()
nome_junto = ''.join(nome_separado)

print(f'Seu nome tem ao todo {len(nome)} letras')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')
