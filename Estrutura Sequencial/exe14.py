peso = float(input('Determine a quantidade pescada no dia: '))
if peso>50:
	excesso = peso-50
	multa = round(excesso*4.5, 2)
	print('O peso excedido foi de: ', excesso, 'Kg')
	print('A multa a ser paga é: R$', multa)
else:
	print('O peso é menor do que 50Kg, então não haverá multa.')
