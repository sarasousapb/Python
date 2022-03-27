numb1 = float(input('Insira o valor do primeiro produto: '))
numb2 = float(input('Insira o valor do segundo produto: '))
numb3 = float(input('Insira o valor do terceiro produto: '))
if numb1 < numb2 and numb1 < numb3:
	print('Deverá ser comprado o primeiro produto, pois custa: R$', numb1)
if numb2 < numb1 and numb2 < numb3:
	print('Deverá ser comprado o segundo produto, pois custa: R$', numb2)
if numb3 < numb1 and numb3 < numb2:
	print('Deverá ser comprado o terceiro produto, pois custa: R$', numb3)
