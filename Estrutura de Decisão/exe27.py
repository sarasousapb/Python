mor = float(input('Insira a quantidade, em kilogramas, de morango adquirido: '))
mac = float(input('Insira a quantidade, em kilogramas, de maçã adquirida: '))
if mor <= 5 and mac <= 5:
	valor_mor = 2.5*mor
	valor_mac = 1.8*mac
	print('Valor total: R$ ', round(valor_mor+valor_mac, 2))
	if (mor + mac) >= 8 or (valor_mor + valor_mac) > 25:
		print('Desconto: R$', round((valor_mor + valor_mac)*0.1, 2), '\nValor total com desconto: R$ ', round((valor_mor + valor_mac)*0.9, 2))
elif mor > 5 and mac > 5:
	valor_mor = 2.2*mor
	valor_mac = 1.5*mac
	print('Valor total: R$ ', round(valor_mor+valor_mac, 2))
	if (mor + mac) >= 8 or (valor_mor + valor_mac) > 25:
		print('Desconto: R$', round((valor_mor + valor_mac)*0.1, 2), '\nValor total com desconto: R$ ', round((valor_mor + valor_mac)*0.9, 2))
elif mor > 5 and mac <= 5:
	valor_mor = 2.2*mor
	valor_mac = 1.8*mac
	print('Valor total: R$ ', round(valor_mor+valor_mac, 2))
	if (mor + mac) >= 8 or (valor_mor + valor_mac) > 25:
		print('Desconto: R$', round((valor_mor + valor_mac)*0.1, 2), '\nValor total com desconto: R$ ', round((valor_mor + valor_mac)*0.9, 2))
elif mor <= 5 and mac > 5:
	valor_mor = 2.5*mor
	valor_mac = 1.5*mac
	print('Valor total: R$ ', round(valor_mor+valor_mac, 2))
	if (mor + mac) >= 8 or (valor_mor + valor_mac) > 25:
		print('Desconto: R$', round((valor_mor + valor_mac)*0.1, 2), '\nValor total com desconto: R$ ', round((valor_mor + valor_mac)*0.9, 2))
