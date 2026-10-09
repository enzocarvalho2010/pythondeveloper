#Fazendo uma calculadora:
print('======================================================Calculadora======================================================')
print('Selecione a operação desejada e depois coloque um ou dois números para realizar o cálculo:')
print('Multiplicação: 1')
print('Divisão: 2')
print('Soma: 3')
print('Subtração: 4')
print('Potenciação: 5')
print('Radiciação: 6')
print('Fatorial: 7')

import math

op = int(input('Digite a operação:'))

if op > 7:
    print('A operação exigida não existe :(')
elif op <= 0:
    print('A operação exigida não existe :(')
elif op == 6:
    n1 = float(input('Digite o número:'))
    f = math.sqrt((n1))
    if f%1 == 0:
        print(f'v({n1}) = {int(f)}')
    else:
        print(f'v({n1}) = {float(f)}')
elif op == 7:
    n1 = int(input('Digite o número:'))
    g = math.factorial((n1))
    print(f'{n1}! = {int(g)}')

else:
    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))
    
    a = n1 * n2
    b = n1 / n2
    c = n1 + n2
    d = n1 - n2
    e = n1 ** n2

    r = [f'{a}',f'{b}',f'{c}',f'{d}',f'{e}']

match op:
    case 1:
        if a%1 == 0:
            print(f'{n1} x {n2} = {int(a)}')
        else:
            print(f'{n1} x {n2} = {float(a)}')
    case 2:
        if b%1 == 0:
            print(f'{n1} : {n2} = {int(b)}')
        else:
            print(f'{n1} : {n2} = {float(b)}')
    case 3:
        if c%1 == 0:
            print(f'{n1} + {n2} = {int(c)}')
        else:
            print(f'{n1} + {n2} = {float(c)}')
    case 4:
        if d%1 == 0:
            print(f'{n1} - {n2} = {int(d)}')
        else:
            print(f'{n1} - {n2} = {float(d)}')
    case 5:
        if e%1 == 0:
            print(f'{n1} ^ {n2} = {int(e)}')
        else:
            print(f'{n1} ^ {n2} = {float(e)}')