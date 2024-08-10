operations = {
    'Soma': '+',
    'Subtração': '-',
    'Multiplicação': '*',
    'Divisão': '/',
    'Exponenciação': '^'
}
while True:
    i = 0
    for op, items in operations.items():
        print('{} - {}'.format(i, op))
        i += 1
    print('\nQual operação você deseja escolher ?\n')

    escolha = int(input())
    if escolha == 0:
        print('Você escolheu a opção {} - {}!'.format(escolha, list(operations.keys())[escolha]))

        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        print('{} + {} = {}\n'.format(x, y, (x + y)))

        print('********************************************************')

        print('Deseja fazer mais alguma operação? 1 - Sim ou 2 - Encerrar')
        esc = int(input())
        if esc == 1:
            continue
        else:
            break

    if escolha == 1:
        print('Você escolheu a opção {} - {}!'.format(escolha, list(operations.keys())[escolha]))

        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        print('{} - {} = {}\n'.format(x, y, (x - y)))

        print('********************************************************')

        print('Deseja fazer mais alguma operação? 1 - Sim ou 2 - Encerrar')

        esc = int(input())
        if esc == 1:
            continue
        else:
            break

    if escolha == 2:
        print('Você escolheu a opção {} - {}!'.format(escolha, list(operations.keys())[escolha]))

        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        print('{} * {} = {}\n'.format(x, y, (x * y)))

        print('********************************************************')

        print('Deseja fazer mais alguma operação? 1 - Sim ou 2 - Encerrar')

        esc = int(input())
        if esc == 1:
            continue
        else:
            break

    if escolha == 3:
        print('Você escolheu a opção {} - {}!'.format(escolha, list(operations.keys())[escolha]))

        x = float(input('Digite o primeiro número: '))
        y = float(input('Digite o segundo número: '))
        print('{} / {} = {}\n'.format(x, y, (x / y)))

        print('********************************************************')

        print('Deseja fazer mais alguma operação? 1 - Sim ou 2 - Encerrar')

        esc = int(input())
        if esc == 1:
            continue
        else:
            break

    if escolha == 4:
        print('Você escolheu a opção {} - {}!'.format(escolha, list(operations.keys())[escolha]))

        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))
        print('{} ^ {} = {}\n'.format(x, y, (x ** y)))

        print('********************************************************')

        print('Deseja fazer mais alguma operação? 1 - Sim ou 2 - Encerrar')

        esc = int(input())
        if esc == 1:
            continue
        else:
            break
