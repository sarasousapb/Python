import math
print('Sabendo que a lei de formação da equação de segundo grau é: ax² + bx + c = 0, determine: ')
a = float(input('O valor de "a": '))
if a != 0:
    b = float(input('O valor de "b": '))
    c = float(input('O valor de "c": '))
    delta = b**2 + (-4 * a * c)
    if delta < 0:
        print('Delta negativo! Não existe valor definido em reais.')
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        print('Delta igual a zero! Existe apenas uma raiz real: x1 = x2 = ', x)
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Delta maior que zero! Existem duas raízes reais: x1 = ', x1, 'e x2 = ', x2)
else:
    print('Valor inválido! A equação não é de segundo grau.')
