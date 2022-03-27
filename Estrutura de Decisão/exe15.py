lado1 = float(input('Insira o valor referente ao primeiro lado: '))
lado2 = float(input('Insira o valor referente ao segundo lado: '))
lado3 = float(input('Insira o valor referente ao terceiro lado: '))
if (lado1 + lado2) > lado3 or (lado1 + lado3) > lado2 or (lado2 + lado3) > lado1:
	if lado1 == lado2 and lado2 == lado3:
		print('A figura plana é um triângulo equilátero, ou seja, possui todos os lado iguais.')
	elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
		print('A figura plana é um triângulo isóceles, ou seja, possui dois lados iguais.')
	elif lado1 != lado2 and lado2 != lado3:
		print('A figura plana é um triângulo escaleno, ou seja, possui três lados com medidas diferentes.')
else:
	print('Valores inválidos! Os valores inseridos não formam um triângulo!')
