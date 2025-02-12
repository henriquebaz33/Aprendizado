nmr = int(input('\033[34mMe diga um número qualquer: \033[m'))

if nmr % 2 == 0:
    print(f'O número {nmr} é \033[34mPAR\033[m')
elif nmr % 2 != 0:
    print(f'O número {nmr} é \033[34mIMPAR\033[m')
    