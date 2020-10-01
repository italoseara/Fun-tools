def SimpleCalc():
    print('{:=^51}'.format(' Simple Calculator '))
    print()

    def again():
        print()
        agn = input('Do you want to calculate again? [y / n] ').lower()
        print()

        if agn == 'y':
            calculator()

        elif agn == 'n':
            print('See you later! :)')
            Start()

        else:
            print('Invalid option!')

    def calculator():
        n1 = float(input('Enter the first number: '))
        n2 = float(input('Enter the second number: '))

        operation = input('''Please, select the operation:
        [ + ] addition
        [ - ] subbtraction
        [ * ] multiplication
        [ / ] division
        [ // ] whole division
        [ ** ] power
        [ new ] enter new numbers
        operation: ''')
        print()

        if operation == '+':
            print('Awnser:', n1 + n2)

        elif operation == '-':
            print('Awnser:', n1 - n2)

        elif operation == '*':
            print('Awnser:', n1 * n2)

        elif operation == '/':
            print('Awnser:', n1 / n2)

        elif operation == '//':
            print('Awnser:', n1 // n2)
            print('Remainder:', n1 % n2)

        elif operation == '**':
            print('Awnser:', n1 ** n2)

        elif operation == 'new':
            calculator()

        else:
            print('invalid operation, try again!')
            calculator()
        again()

    calculator()


def LawofCosines():
    from math import cos, radians

    print('{:=^40}'.format(' Cossine Law '))
    print()
    a = float(input('1st Side: '))
    b = float(input('2nd Side: '))
    angle = float(input('Angle: '))
    c = (a ** 2 + b ** 2 - 2 * a * b * cos(radians(angle))) ** 0.5
    print()
    print('R = √(a² + b² - 2.a.b.cos(x))')
    print('R = √({}² + {}² - 2.{}.{}.cos({}))'.format(a, b, a, b, angle))
    print('R = √({} + {} - {}.{:.1f})'.format(a ** 2, b ** 2, 2 * a * b, cos(radians(angle))))
    print('R = √({} - {:.1f})'.format(a ** 2 + b ** 2, (2 * a * b) * cos(radians(angle))))
    print('R = √{}'.format(a ** 2 + b ** 2 - 2 * a * b * cos(radians(angle))))
    print('R = {}'.format(c))
    Start()


def FibonacciSequence():
    terms = int(input('How many terms should the sequence have? '))
    t1 = 0
    t2 = 1
    cont = 0
    if terms == 1:
        print('0 -> END')
    else:
        print('0 -> 1 ->', end=' ')
        while terms - 2 != cont:
            cont += 1
            t3 = t2 + t1
            t2 = t3
            t1 = t2
            print('{} ->'.format(t3), end=' ')
        print('END')
    Start()


def Factorial():
    print('{:=^51}'.format(' Factorial Calculator '))
    print()
    n = int(input('Factorial of: '))
    fat = 1
    print('{}! ='.format(n), end=' ')
    for c in range(n, 0, -1):
        print(c, end=' ')
        if c != 1:
            print('.', end=' ')
        else:
            print('=', end=' ')
        fat = fat * c
    print(fat)
    Start()


def Retangle():
    base = int(input('Base: '))
    high = int(input('High: '))
    print()
    print('*' * base)
    cont = high + 1
    while cont > 2:
        print('*', end='')
        print(' ' * (base - 2), end='')
        print('*')
        cont = cont - 1
    print('*' * base)
    Start()


def Triangle():
    bh = int(input('Base == High: '))
    print()
    print('*')
    cont = 0
    while cont < (bh - 2):
        print('*', end='')
        print(' ' * cont, end='')
        print('*')
        cont += 1
    print('*' * bh)
    Start()


def MultiplicationTable():
    num = int(input('Enter a Number: '))
    n = 0
    print()
    print('-' * 15)
    for c in range(1, 11):
        n += 1
        print('{} x {} = {}'.format(num, n, num * n))
    print('-' * 15)
    Start()


def ArithmeticProgression():
    pt = int(input('First Term: '))
    razao = int(input('Reason: '))
    cont = 0
    while cont != 10:
        cont += 1
        print('{} ->'.format(pt), end=' ')
        pt = pt + razao
    print('END')
    Start()


def SecondDegree():
    equa = str(input('Enter the Equation: '))
    a = equa[:equa.find('x²')]
    if a == '':
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)
    b = equa[equa.find('x² ') + 2:equa.rfind('x ')]
    if b == ' +':
        b = 1
    elif b == ' -':
        b = -1
    else:
        b = int(b)
    c = int(equa[equa.rfind('x ') + 1:equa.rfind(' =')])
    d = int(equa[equa.rfind(' '):])
    c = c + (d * -1)
    delta = b ** 2 - 4 * a * c
    print('Δ = b² -4ac')
    print('Δ = {}² -2.{}.{}'.format(b, a, c))
    print('Δ = {} - {}'.format(b ** 2, 4 * a * c))
    print('Δ = {}'.format(delta))
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print()
    print('x = (–b ± √∆) / (2.a)')
    print('x = ({} ± √{}) / (2.{})'.format(b * -1, delta, a))
    print('x = ({} ± {}) / {}'.format(b * -1, delta ** 0.5, a * 2))
    print()
    print('x¹ = ({} + {}) / {}'.format(b * -1, delta ** 0.5, a * 2))
    print('x¹ = {} / {}'.format((b * -1) + (delta ** 0.5), a * 2))
    print('x¹ = {}'.format(x1))
    print()
    print('x² = ({} - {}) / {}'.format(b * -1, delta ** 0.5, a * 2))
    print('x² = {} / {}'.format((b * -1) - (delta ** 0.5), a * 2))
    print('x² = {}'.format(x2))
    Start()


def Start():
    from time import sleep

    sleep(1)
    print()
    print('='*51)
    print()
    aw = input('''[ 1 ] Simple Calculator
[ 2 ] Factorial
[ 3 ] Second Degree Equation
[ 4 ] Multiplication Table
[ 5 ] Arithmetic Progression
[ 6 ] Fibonacci Sequence
[ 7 ] Law of Cosines
[ 8 ] Retangle
[ 9 ] Triangle
Select a option: ''')
    print()
    if aw == '1':
        print('Initializing...')
        sleep(0.5)
        print()
        SimpleCalc()
    elif aw == '2':
        print('Initializing...')
        sleep(0.5)
        print()
        Factorial()
    elif aw == '3':
        print('Initializing...')
        sleep(0.5)
        print()
        SecondDegree()
    elif aw == '4':
        print('Initializing...')
        sleep(0.5)
        print()
        MultiplicationTable()
    elif aw == '5':
        print('Initializing...')
        sleep(0.5)
        print()
        ArithmeticProgression()
    elif aw == '6':
        print('Initializing...')
        sleep(0.5)
        print()
        FibonacciSequence()
    elif aw == '7':
        print('Initializing...')
        sleep(0.5)
        print()
        LawofCosines()
    elif aw == '8':
        print('Initializing...')
        sleep(0.5)
        print()
        Retangle()
    elif aw == '9':
        print('Initializing...')
        sleep(0.5)
        print()
        Triangle()


Start()
