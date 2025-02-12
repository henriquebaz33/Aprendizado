nmr1 = int(input('Primeiro valor: '))
nmr2 = int(input('Segundo valor: '))
nmr3 = int(input('Terceiro valor: '))

menor = nmr1
maior = nmr1

if nmr2 < menor and nmr2 < nmr3:   
    menor = nmr2
elif nmr3 < menor:
    menor = nmr3

if nmr2 > maior and nmr2 > nmr3:
    maior = nmr2
elif nmr3 > maior:
    maior = nmr3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
