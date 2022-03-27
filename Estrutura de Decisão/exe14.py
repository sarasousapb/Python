nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
media = ((nota1 + nota2)/2)
if media > 9 and media <= 10:
    print('APROVADO! Média:', media, ', Conceito: A')
elif media > 7.5 and media <= 9:
    print('APROVADO! Média:', media, ', Conceito: B')
elif media > 6 and media <= 7.5:
    print('APROVADO! Média:', media, ', Conceito: C')
elif media > 4 and media <= 6:
    print('REPROVADO! Média:', media, ', Conceito: D')
elif media >= 0 and media <= 4:
    print('REPROVADO! Média:', media, ', Conceito: E')
else:
    print('Valores inválidos.')
