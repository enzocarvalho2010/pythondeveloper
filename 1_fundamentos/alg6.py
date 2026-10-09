#Leia três notas e mostre a média de um aluno:
nome = str(input('Digite o nome do aluno:'))
n1 = int(input('Digite a nota 1:'))
n2 = int(input('Digite a nota 2:'))
n3 = int(input('Digite a nota 3:'))

soma = n1 + n2 + n3
m = (soma)/3
media = int(m)

print(f'A média de {nome} é {media}')

if media >=6:
    print(f'O aluno {nome} tirou a nota {media}, portanto, passou de ano!')

else:
    print(f'O aluno {nome} tirou a nota {media}, portanto, ficou de recuperação...')
