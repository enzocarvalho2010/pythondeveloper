#teclado
nome = str(input("digite o seu nome"))
idade = int(input("digite a sua idade"))
if idade >=18:
    r1 = (f'O {nome} está mentindo, pois não é maior de idade!')
    print(r1)
else:
    r = (f'O {nome} é menor de idade!')
    print(r)   
print('Programa encerrado com sucesso...')