'''
Ler o nome do aluno
Ler o número da turma
Ler três notas
'''
'''
Calcular a média
Verificar status
'''
nome = str(input('Digite o nome do aluno:'))

turma = int(input('Digite o número da turma do aluno:'))

n1 = float(input('Digite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
n3 = float(input('Digite a terceira nota do aluno:'))

soma = n1 + n2 + n3
m = (soma)/3

if m >= 7:
    print(f'Soma das notas: {soma}')
    print(f'Nota final: {m}')
    print(f'O aluno {nome} da turma {turma} foi aprovado!!!')
else:
    print(f'Soma das notas: {soma}')
    print(f'Nota final: {m}')
    print(f'O aluno {nome} da turma {turma} foi reprovado...')