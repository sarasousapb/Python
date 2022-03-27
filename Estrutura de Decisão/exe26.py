comb = input('Sabendo que: \n(A) - Álcool; \n(G) - Gasolina. \nDefina o combusível escolhido: ')
quant = float(input('Insira a quantidade de combustível adquirida (em litros): '))
if comb == ('A'):
	if quant <= 20:
		print('O valor pago será de: R$', round(1.9*quant*0.97, 2))
	elif quant > 20:
		print('O valor pago será de: R$', round(1.9*quant*0.95, 2))
elif comb == ('G'):
	if quant <= 20:
		print('O valor pago será de: R$', round(2.5*quant*0.96, 2))
	elif quant > 20:
		print('O valor pago será de: R$', round(2.5*quant*0.94, 2))
else:
	print('Escolha inválida.')
