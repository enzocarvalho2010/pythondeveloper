d = int(input('digite um número'))

match d:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terça')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sábado')
    case _:
        print('dia inexstente')