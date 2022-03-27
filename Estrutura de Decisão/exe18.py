dia = int(input('Insira um valor referente ao dia: '))
mes = int(input('Insira um valor referente ao mês: '))
ano = int(input('Insira um valor referente ao ano: '))
if (ano%4 == 0):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >=1 and dia <= 31:
            print('Data válida!')
        else:
            print('Data inválida!')
    elif mes == 2:
        if dia >= 1 and dia <= 29:
            print('Data válida!')
        else:
            print('Data inválida!')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >=1 and dia <= 30:
            print('Data válida!')
        else:
            print('Data inválida!')
    else:
        print('Data inválida!')
else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print('Data válida!')
        else:
            print('Data inválida!')
    elif mes == 2:
        if dia >= 1 and dia <= 28:
            print('Data válida!')
        else:
            print('Data inválida!')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print('Data válida!')
        else:
            print('Data inválida!')
    else:
        print('Data inválida!')
