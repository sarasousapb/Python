valor = float(input('Insira um valor: '))
if valor < 1000:
	print(valor, ' = ', int(valor/100), 'centena(s), ', int((valor%100)/10), ' dezena(s) e ', int((valor%100)%10), ' unidade(s)')
else:
	print('Valor inválido!')
