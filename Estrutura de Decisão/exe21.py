import math
print('Sabendo que o limite mínimo de saque é R$10,00 e o limite máximo é R$600,00.')
valor = int(input('Insira o valor que deseja sacar: R$ '))
if valor >= 10 and valor <= 600:
	cem = math.floor(valor/100)
	cinq = math.floor((valor%100)/50)
	dez = math.floor(((valor%100)%50)/10)
	cinco = math.floor(int(((valor%100)%50)%10)/5)
	um = math.floor((((valor%100)%50)%10)%5)
	print('Serão disponibilizadas: ', cem, ' nota(s) de R$100,00, ', cinq, ' nota(s) de R$50,00, ', dez, ' nota(s) de R$10,00, ', cinco, ' nota(s) de R$5,00 e ', um, ' nota(s) de R$1,00.')
	print('Totalizando o valor completo de R$ ', valor, ',00')
else:
	print('Valor inválido!')
# Math.floor arredonda para um número inteiro, abaixo do número resultado.
