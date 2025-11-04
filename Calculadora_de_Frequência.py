total_aulas = int(input('Digite o total de aulas NO ANO: '))
faltas = int(input('Digite a quantidade de faltas NO ANO todo: '))


total = 0
for f in range(1, 5):
    bim = int(input(f'Digite a quantidade de aulas do {f}° bimestre '))
    total += bim
calc = ((total - faltas) / (total) * 100)
print('A sua frequência escolar é {:.2f}%'.format(calc))

if calc < 75:
    print('Você está com risco de reprovar!!!!')
else:
    print('Você não tem riscode reprovar!!!')