unidade = ['um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove']
onze_a_dezenove = ['onze', 'doze', 'treze', 'quatorze',
                   'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezena = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta',
          'sessenta', 'setenta', 'oitenta', 'noventa']
centena = ['cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos',
           'novecentos']
centena2 = ['cento']

cont = 0
lista = list()

lista = list(input('Número de 5 digitos: '))
for x in range(len(lista)):
    lista[x] = int(lista[x])

if lista[0] == 1 and lista[1] != 0:
    milh = onze_a_dezenove[lista[1] - 1]

elif lista[1] == 0:
    milh = dezena[lista[0] - 1]

elif lista[0] != 1 and lista[1] != 0:
    a1 = dezena[lista[0] - 1]
    b1 = unidade[lista[1] - 1]
    milh = a1 + ' e ' + b1

if lista[2] == 1:
    cent = centena2[0]

else:
    cent = centena[lista[2] - 1]

if lista[3] == 1 and lista[4] != 0:
    deze = onze_a_dezenove[lista[4] - 1]

elif lista[2] != 0 and lista[3] == lista[4] == 0:
    deze = centena[lista[2] - 1]

elif lista[3] != 1 and lista[4] != 0:
    a2 = dezena[lista[3] - 1]
    b2 = unidade[lista[4] - 1]
    deze = a2 + ' e ' + b2

elif lista[3] != 1 and lista[4] == 0:
    deze = dezena[lista[3] - 1]

else:
    deze = dezena[0]

if lista[2] == lista[3] == lista[4] == 0:
    print(f'\nO número digitado foi: {milh.title()} Mil')

elif lista[3] == lista[4] == 0 and lista[2] != 0:
    print(f'\nO número digitado foi: {milh.title()} Mil e {cent.title()}')
else:
    print(
        f'\nO número digitado foi: {milh.title()} Mil {cent.title()} e {deze.title()}')
