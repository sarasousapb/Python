nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
media = round((nota1+nota2+nota3+nota4)/4, 2)
print('A média das notas inseridas é: ', media)
if media >= 7:
	print('APROVADO!')
else:
	print('REPROVADO!')
