print('Responda as perguntas abaixo com: \n(1) - Sim; \n(0) - Não.')
tel = int(input('Telefonou para a vítima? '))
if (tel != 0) and (tel != 1):
	print('Valor inválido!')
else:
	loc = int(input('Esteve no local do crime? '))
	if loc != 0 and loc != 1:
		print('Valor inválido!')
	else:
		prox = int(input('Mora perto da vítima? '))
		if prox != 0 and prox != 1:
			print('Valor inválido!')
		else:
			din = int(input('Devia para a vítima? '))
			if din != 0 and din != 1:
				print('Valor inválido!')
			else:
				trab = int(input('Já trabalhou com a vítima? '))
				if trab != 0 and trab != 1:
					print('Valor inválido!')
				else:
					if (tel + loc + prox + din + trab) == 0 or (tel + loc + prox + din + trab) == 1:
						print('Não suspeito(a).')
					elif (tel + loc + prox + din + trab) == 2:
						print('Suspeito(a).')
					elif (tel + loc + prox + din + trab) == 3 or (tel + loc + prox + din + trab) == 4:
						print('Cúmplice.')
					elif (tel + loc + prox + din + trab) == 5:
						print('Assassino.')
					else:
						print('Valor inválido.')
