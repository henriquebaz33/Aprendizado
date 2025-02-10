nome_completo = str(input("Digite seu nome completo: ")).lower().strip().split()

print(f'Seu primeiro nome é {nome_completo[0].capitalize()}')
print(f'Seu último nome é {nome_completo[len(nome_completo) - 1].capitalize()}')
