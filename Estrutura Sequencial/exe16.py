import math
area = float(input('Informe a área que será pintada: '))
latas = math.ceil(area/54)
valor = latas*80
print('Serão necessárias', latas, 'lata(s) de tinta, e o valor total é de R$', valor, ',00')
# math.ceil( ) - arredondar para cima
# math.floor( ) - arredondar para baixo
