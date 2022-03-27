numb1 = float(input('Insira o primeiro número: '))
numb2 = float(input('Insira o segundo número: '))
numb3 = float(input('Insira o terceiro número: '))
if numb1 > numb2 and numb1 < numb3:
	print('O maior número é o: ', numb3, 'e o menor número é o: ', numb2)
if numb1 > numb3 and numb1 < numb2:
	print('O maior número é o: ', numb2, 'e o menor número é o: ', numb3)
if numb2 > numb3 and numb2 < numb1:
	print('O maior número é o: ', numb1, 'e o menor número é o: ', numb3)
if numb2 > numb1 and numb2 < numb3:
	print('O maior número é o: ', numb3, 'e o menor número é o: ', numb1)
if numb3 > numb1 and numb3 < numb2:
	print('O maior número é o: ', numb2, 'e o menor número é o: ', numb1)
if numb3 > numb2 and numb3 < numb1:
	print('O maior número é o: ', numb1, 'e o menor número é o: ', numb2)
