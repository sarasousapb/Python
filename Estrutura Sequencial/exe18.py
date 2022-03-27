tamanho = float(input('Insira o tamanho do arquivo (em MB): '))
velocidade = float(input('Insira a velocidade de download (em Mbps): '))
print('O tempo estimado para a conclusão do download é de: ', round((tamanho/velocidade), 2) , 'segundos')
