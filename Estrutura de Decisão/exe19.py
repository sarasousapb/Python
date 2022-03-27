valor = float(input('Insira um valor: '))
if valor < 1000:
	print(valor, ' = ', int(valor/100), 'centena(s), ', int((valor%100)/10), ' dezena(s) e ', int((valor%100)%10), ' unidade(s)')
else:
	print('Valor inválido!')

QUESTÃO 20
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
	print('Média: ', media, '- Aprovado com distinção!')
elif media >= 7 and media < 10:
	print('Média: ', media, '- Aprovado!')
elif media < 7:
	print('Média: ', media, '- Reprovado!')
else:
	print('Valor inválido!')
