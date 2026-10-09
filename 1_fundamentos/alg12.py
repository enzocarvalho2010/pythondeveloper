'''
Crie um algorítmo que leia dois números
Mostre no final qual número é o maior
'''
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))

if n1 > n2:
    print(f'{n1} é o maior número.')
elif n1 == n2:
    print(f'Os dois números são iguais.')
else:
    print(int(f'{n2} é o maior número.'))