valor_hora = float(input('Insira o valor da hora/homem: '))
horas_trab = int(input('Insira quantas horas foram trabalhadas no mês: '))
salario_bruto = valor_hora*horas_trab
ir = (salario_bruto*11)/100
inss = (salario_bruto*8)/100
sindicato = (salario_bruto*5)/100
salario_liq = salario_bruto-(ir+inss+sindicato)
print('+ Salário bruto: R$', salario_bruto)
print('- IR: R$', ir)
print('- INSS: R$', inss)
print('- Sindicato: R$', sindicato)
print('= Salário líquido: R$', salario_liq)
