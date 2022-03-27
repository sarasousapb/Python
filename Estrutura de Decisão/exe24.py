numb1 = float(input('Insira o primeiro valor: '))
numb2 = float(input('Insira o segundo valor: '))
escolha = int(input('Sabendo que as operações disponíveis são: \n(1) - Saber se os números são pares ou ímpares; \n(2) - Saber se os números são positivos ou negativos; \n(3) - Saber se os números são inteiros ou decimais. \nDetermine sua escolha: '))
if (escolha == 1):
	if numb1%2 == 0 and numb2%2 == 0:
		print('Ambos os números são pares.')
	elif numb1%2 != 0 and numb2%2 != 0:
		print('Ambos os números são ímpares.')
	elif numb1%2 == 0 and numb2%2 != 0:
		print('O número ', numb1, ' é par, e o número ', numb2, ' é ímpar.')
	elif numb1%2 != 0 and numb2%2 == 0:
		print('O número ', numb1, ' é ímpar, e o número ', numb2, ' é par.')
elif escolha == 2:
	if numb1 >= 0 and numb2 >= 0:
		print('Ambos os números são positivos.')
	elif numb1 < 0 and numb2 < 0:
		print('Ambos os números são negativos.')
	elif numb1 >= 0 and numb2 < 0:
		print('O número ', numb1, 'é positivo e o número ', numb2, ' é negativo.')
	elif numb1 < 0 and numb2 >= 0:
		print('O número ', numb1, 'é negativo e o número ', numb2, ' é positivo.')
elif escolha == 3:
	if numb1%1 == 0 and numb2%1 == 0:
		print('Ambos os números são inteiros.')
	elif numb1%1 != 0 and numb2%1 != 0:
		print('Ambos os números são decimais.')
	elif numb1%1 == 0 and numb2%1 != 0:
		print('O número ', numb1, ' é inteiro e o número ', numb2, ' é decimal.')
	elif numb1%1 != 0 and numb2%1 == 0:
		print('O número ', numb1, ' é decimal e o número ', numb2, ' é inteiro.')
else:
	print('Escolha inválida!')
