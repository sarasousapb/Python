import math
area = float(input('Informe a área a ser pintada: '))
apenas_latas = math.ceil(area*1.1/108)
apenas_galoes = math.ceil(area*1.1/21.6)
int_latas = round((area*1.1)/108, 0)
resto_galoes = math.ceil(((area*1.1)%108)/21.6)
print('Opção I: Serão necessárias', apenas_latas, 'lata(s) de tinta, e o valor total é de R$', apenas_latas*80, ',00')
print('Opção II: Serão necessários', apenas_galoes, 'galão(ões) de tinta, e o valor total é de R$', apenas_galoes*25, ',00')
print('Opção III: Serão necessários', int_latas, 'lata(s) de tinta, e', resto_galoes, 'galão(ões) de tinta. O valor total é de: R$', round(((int_latas*80)+(resto_galoes*25)), 0), ',00')
# Nas opções há o acréscimo de 10% para margem de erro de pintura, conforme solicitado
