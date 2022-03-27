salario = float(input('Insira o valor do salário atual: '))
if salario <= 280:
	print('O valor inicial ddo salário atual é de: R$', salario, '\n O percentual de aumento aplicado foi de: 20% \n O valor do aumento foi de: R$', round(salario*0.2, 2), '\n O valor final do salário, após o reajuste é de: R$', round(salario*1.2, 2))
if salario > 280 and salario <= 700:
	print('O valor inicial ddo salário atual é de: R$', salario, '\n O percentual de aumento aplicado foi de: 15% \n O valor do aumento foi de: R$', round(salario*0.15, 2), '\n O valor final do salário, após o reajuste é de: R$', round(salario*1.15, 2))
if salario > 700 and salario <= 1500:
	print('O valor inicial ddo salário atual é de: R$', salario, '\n O percentual de aumento aplicado foi de: 10% \n O valor do aumento foi de: R$', round(salario*0.1, 2), '\n O valor final do salário, após o reajuste é de: R$', round(salario*1.1, 2))
if salario > 1500:
	print('O valor inicial ddo salário atual é de: R$', salario, '\n O percentual de aumento aplicado foi de: 5% \n O valor do aumento foi de: R$', round(salario*0.05, 2), '\n O valor final do salário, após o reajuste é de: R$', round(salario*1.05, 2))
