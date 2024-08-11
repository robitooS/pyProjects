carros = [
    ['Chevrolet Tracker', 120],
    ['Chevrolet Onix', 90],
    ['Chevrolet Spin', 150],
    ['Hyundai HB20', 85],
    ['Fiat Uno', 60]
]

carros_alugados = []


def mostrar_array(array):
    op = 0
    for carro, valor in array:
        print('[{}] {} - R$ {} /dia'.format(op, carro, valor))
        op += 1


while True:
    print('''
    ========================================
        Bem vindo á locadora de carros!
    ========================================    
    
    O que deseja fazer? 
    0 - Mostrar portfólio | 1 - Alugar um carro | 2 - Devolver um carro
    ''')
    escolha = int(input())

    if escolha == 0:
        mostrar_array(carros)

        print('\n\n===========================\n 0 - CONTINUAR | 1 - SAIR')
        escolha = int(input())
        if escolha == 1:
            break

    if escolha == 1:
        print('[ ALUGAR ] Dê uma olhada em nosso portfólio.\n')
        mostrar_array(carros)

        print('===========================\nEscolha o código do carro:')
        cod = int(input())

        print('===========================\nEscolha por quantos dias você quer alugar o carro:')
        dias = int(input())

        print('''
        Você escolheu {} por {} dias
        O aluguel totalizaria R$ {}. Deseja alugar?\n\n0 - Sim 1 - Não
        '''.format(carros[cod][0], dias, (carros[cod][1] * dias)))
        escolha = int(input())

        if escolha == 0:
            print('\nParabéns você alugou o {} por {} dias'.format(carros[cod][0], dias))
            carros_alugados.append(carros.pop(cod))

        elif escolha == 1:
            print('\nCancelada a operação!')
        continue

        print('\n\n===========================\n 0 - CONTINUAR | 1 - SAIR')
        escolha = int(input())
        if escolha == 1:
            break

    if escolha == 2:

        if len(carros_alugados) > 0:
            print('\nSegue a lista dos carros alugados:\n')
            mostrar_array(carros_alugados)

            print('Escolha o código do carro que deseja devolver: ')
            escolha = int(input())

            print('Carro devolvido com sucesso!')
            carros.append(carros_alugados.pop(escolha))

            print('\n\n===========================\n 0 - CONTINUAR | 1 - SAIR')
            escolha = int(input())
            if escolha == 1:
                break
        else:
            print('Não há carros alugados no momento!')
