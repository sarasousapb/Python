numb1 = float(input('Insira o primeiro número: '))
numb2 = float(input('Insira o segundo número: '))
numb3 = float(input('Insira o terceiro número: '))
if numb1 > numb2 and numb1 > numb3:
	print('O primeiro número inserido é o maior, número: ', numb1)
if numb2 > numb1 and numb2 > numb3:
	print('O segundo número inserido é o maior, número: ', numb2)
if numb3 > numb1 and numb3 > numb2:
	print('O terceiro número inserido é o maior, número: ', numb3)
