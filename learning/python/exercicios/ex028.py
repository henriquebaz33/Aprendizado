from time import sleep
from random import randint
import os


nmr = -1

while nmr > 5 or nmr < 0:
    os.system("cls")
    print('\033[33m-=-\033[0m' * 20)
    print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[0m')
    print('\033[33m-=-\033[0m' * 20)
    nmr = int(input("Em que número eu pensei? "))
    sleep(0.6)

print("\033[35mPROCESSANDO...\033[0m")
sleep(1)

nmr_computador = randint(0, 5)

if nmr_computador != nmr:
    print(f'\033[31mGANHEI! Eu pensei no número {nmr_computador} e não no {nmr}!\033[0m')
elif nmr_computador == nmr:
    print(f'\033[33mPARABÉNS! Você conseguiu me vencer!\033[m')


print()
