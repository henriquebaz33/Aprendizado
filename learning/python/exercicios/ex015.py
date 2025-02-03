dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = float(input("Quandtos Km rodados? "))

total_pagar = (dias_alugados * 60) + (km_rodados * 0.15)

print(f'O total a pagar é de R${total_pagar:.2f}')
