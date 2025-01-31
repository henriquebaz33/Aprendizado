largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print(f'Sua parede tem a dimensão de {largura:.1f}x{altura:.1f} e sua área é de {area}m²')

print(f'Para pintar essa parede, você precisará de {area / 2}l de tinta')
