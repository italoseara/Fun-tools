from time import sleep


def codificador():

    print('\nEvite o uso de acentos!')

    mensagem = str(input('Mensagem: ')).upper()

    if len(mensagem) % 2 != 0:
        mensagem += ' '

    a = [[5, 7],
         [2, 3]]

    tabela = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', '.', ',', '!', ' ', '_']

    original = [[], []]

    codificada = [[], []]

    mensagemcod = ''

    for x in range(len(mensagem)):
        for y in range(len(tabela)):
            if mensagem[x] == tabela[y]:
                if x < len(mensagem) // 2:
                    original[0].append(y + 1)
                else:
                    original[1].append(y + 1)

    for p in range(len(original[0])):

        for i in range(len(a)):

            if i == 0:
                codificada[0].append(a[0][0] * original[0][p] + a[0][1] * original[1][p])

            elif i == 1:
                codificada[1].append(a[1][0] * original[0][p] + a[1][1] * original[1][p])

    for x, y in enumerate(codificada[0]):
        mensagemcod += f'{y}, '

    for x, y in enumerate(codificada[1]):
        if x != len(codificada[1]) - 1:
            mensagemcod += f'{y}, '
        else:
            mensagemcod += f'{y}'

    print(f'''
Mensagem: {mensagem}

Matriz gerada: 
{original[0]}
{original[1]}

Matriz de Codificação:
{a[0]}
{a[1]}

Matriz Codificada:
{codificada[0]}
{codificada[1]}

Mensagem Codificada:
{mensagemcod}''')


def decodificador():

    while True:
        senha = int(input('\nDigite a senha: '))

        print('\nPROCESSANDO...\n')
        sleep(2)

        if senha == 131023335689:
            print('Senha correta! Acesso Liberado\n')
            break

        else:
            print('Senha Incorreta! Tente Novamente\n')

    codificada1 = []

    codificada = [[], []]

    decodificada = [[], []]

    inversa = [[3, -7],
               [-2, 5]]

    tabela = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z', '.', ',', '!', ' ', '_']

    mensagemcod = str(input('Mensagem Codificada: '))

    num = ''

    mensagem = ''

    for x, y in enumerate(mensagemcod):
        if y != ',' and y != ' ':

            num += y

        if y == ',' or x == len(mensagemcod) - 1:

            codificada1.append(int(num))

            num = ''

    for x in range(len(codificada1)):

        if x < len(codificada1) / 2:
            codificada[0].append(codificada1[x])

        else:
            codificada[1].append(codificada1[x])

    for p in range(len(codificada[0])):

        for i in range(len(inversa)):

            if i == 0:
                decodificada[0].append(inversa[0][0] * codificada[0][p] + inversa[0][1] * codificada[1][p])

    for p in range(len(codificada[1])):

        for i in range(len(inversa)):

            if i == 1:

                decodificada[1].append(inversa[1][0] * codificada[0][p] + inversa[1][1] * codificada[1][p])

    for x in range(len(decodificada)):
        for y in range(len(decodificada[x])):
            mensagem += tabela[decodificada[x][y] - 1]

    print(f'''
Matriz Codificada:
{codificada[0]}
{codificada[1]}

Matriz Inversa:
{inversa[0]}
{inversa[1]}

Matriz Decodificada:
{decodificada[0]}
{decodificada[1]}

Mensagem: {mensagem}''')


while True:
    painel = int(input('''\nSelecione uma função:
    [ 1 ] Codificador
    [ 2 ] Decodificador
    [ 3 ] Sair
'''))

    if painel == 1:
        codificador()

    elif painel == 2:
        decodificador()

    elif painel == 3:
        print('\nFINALIZANDO...')
        sleep(2)
        print('Até outro dia!')
        break
