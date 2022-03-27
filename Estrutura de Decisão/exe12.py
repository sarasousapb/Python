valor_hora = float(input('Insira o valor referente à hora trabalhada: R$ '))
horas_trab = float(input('Insira quantas horas foram trabalhadas no mês: '))
salario_bruto = valor_hora*horas_trab
if salario_bruto <= 900:
	print('Salário bruto: (', valor_hora, '*', horas_trab, '): R$ ', round(salario_bruto, 2), '\n (-) IR (0%): R$ ', round(salario_bruto*0, 2), '\n (-) INSS (10%): R$ ', round(salario_bruto*0.1, 2), '\n FGTS (11%): R$ ', round(salario_bruto*0.11, 2), '\n Total dos descontos: R$' , round(salario_bruto*0.1, 2), '\n Salário líquido: R$ ', round(salario_bruto*0.9, 2))
elif salario_bruto > 900 and salario_bruto <= 1500:
	print('Salário bruto: (', valor_hora, '*', horas_trab, '): R$ ', round(salario_bruto, 2), '\n (-) IR (5%): R$ ', round(salario_bruto*0.05, 2), '\n (-) INSS (10%): R$ ', round(salario_bruto*0.1, ), '\n FGTS (11%): R$ ', round(salario_bruto*0.11, 2), '\n Total dos descontos: R$' , round(salario_bruto*(0.05+0.1), 2), '\n Salário líquido: R$ ', round(salario_bruto*0.85, 2))
elif salario_bruto > 1500 and salario_bruto <= 2500:
	print('Salário bruto: (', valor_hora, '*', horas_trab, '): R$ ', round(salario_bruto, 2), '\n (-) IR (10%): R$ ', round(salario_bruto*0.1, 2), '\n (-) INSS (10%): R$ ', round(salario_bruto*0.1, ), '\n FGTS (11%): R$ ', round(salario_bruto*0.11, 2), '\n Total dos descontos: R$' , round(salario_bruto*(0.1+0.1), 2), '\n Salário líquido: R$ ', round(salario_bruto*0.8, 2))
elif salario_bruto > 2500:
	print('Salário bruto: (', valor_hora, '*', horas_trab, '): R$ ', round(salario_bruto, 2), '\n (-) IR (20%): R$ ', round(salario_bruto*0.2, 2), '\n (-) INSS (10%): R$ ', round(salario_bruto*0.1, ), '\n FGTS (11%): R$ ', round(salario_bruto*0.11, 2), '\n Total dos descontos: R$' , round(salario_bruto*(0.2+0.1), 2), '\n Salário líquido: R$ ', round(salario_bruto*0.7, 2))
