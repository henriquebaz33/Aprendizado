nmr = int(input('Informe um número: '))

unidade = nmr // 1 - (nmr // 10 * 10)
print(f'Unidade: {unidade}')

dezena = nmr // 10 - (nmr // 100 * 10)
print(f'Dezena: {dezena}')

centena = nmr // 100 - (nmr // 1000 * 10)
print(f'Centena: {centena}')

milhar = nmr // 1000 - (nmr // 10000 * 10)
print(f'Milhar: {milhar}')
