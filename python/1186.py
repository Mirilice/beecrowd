operacao = input()

soma = 0
cont = 0

for i in range(12):
    for j in range(12):
        num = float(input())
        if(j+i >= 12):
            soma += num
            cont+=1


if operacao == 'S':
    print(f'{soma:.1f}')
else: print(f'{soma/cont:.1f}')
