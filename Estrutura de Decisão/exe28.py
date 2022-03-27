tipo_carne = int(input('Tipos de carne: \n(1) - Filé duplo; \n(2) - Alcatra; \n(3) - Picanha. \nEscolha um tipo de carne: '))
quant = float(input('Insira a quantidade, em kilogramas, da carne escolhida: '))
fop = int(input('Forma de pagamento: \n(1) - Cartão Tabajara; \n(2) - Cartão de crédito ou débito; \n(3) - Espécie. \nDetermine a forma de pagamento: '))
if tipo_carne == 1:
	if quant <= 5:
		valor_total = round(4.9*quant, 2)
	elif quant > 5:
		valor_total = round(5.8*quant, 2)
elif tipo_carne == 2:
	if quant <= 5:
		valor_total = round(5.9*quant, 2)
	elif quant > 5:
		valor_total = round(6.8*quant, 2)
elif tipo_carne == 3:
	if quant <= 5:
		valor_total = round(6.9*quant, 2)
	elif quant > 5:
		valor_total = round(7.8*quant, 2)
if fop == 1:
	print('CUPOM FISCAL \nTipo de carne: ', tipo_carne, '\nQuantidade de carne: ', quant, 'Kg \nPreço total: R$', round(valor_total, 2), '\nForma de pagamento: ', fop, '\nValor do desconto: R$', round(valor_total*0.05, 2), '\nValor total com desconto: R$', round(valor_total*0.95, 2))
elif fop == 2 or fop == 3:
	print('CUPOM FISCAL \nTipo de carne: ', tipo_carne, '\nQuantidade de carne: ', quant, 'Kg \nPreço total: R$', round(valor_total, 2), '\nForma de pagamento: ', fop, '\nValor do desconto: R$', round(valor_total*0, 2), '\nValor total com desconto: R$', round(valor_total, 2))
else:
	print('Valor inválido!')
