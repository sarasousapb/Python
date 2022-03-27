turno = input('Sendo, M - matutino, V - vespertino e N - noturno, insira o turno de estudo: ')
if turno == 'M':
	print('Bom dia!')
elif turno == 'V':
	print('Boa tarde!')
elif turno == 'N':
	print('Boa noite!')
elif turno != 'M' and turno != 'V' and turno != 'N':
	print('Valor inválido!')
