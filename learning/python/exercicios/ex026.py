frase = str(input("Digite uma frase: ")).lower()

print(f"A letra A apareceu {frase.count("a")} vezes na frase")
print(f"A primeira letra A apareceu na posição {frase.strip().find("a") + 1}")
print(f'A última letra A apareceu na posição {frase.strip().rfind("a") + 1}')
