altura = float(input('Insira sua altura: '))
sexo = input('Você se identifica com o sexo feminino ou masculino? ')
if (sexo == 'feminino'):
	peso = round((62.1 * altura) - 44.7, 2)
	print('Seu peso ideal é: ', peso)
else:
	peso = round((72.7 * altura) - 58, 2)
	print('Seu peso ideal é: ', peso)
