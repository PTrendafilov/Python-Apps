def add(a, b):
    answer = a + b
    print(f'{a} + {b} = {answer}')


def sub(a, b):
    answer = a - b
    print(f'{a} - {b} = {answer}')


def mul(a, b):
    answer = a * b
    print(f'{a} * {b} = {answer}')


def div(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer}')


while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('E. Exit')
    choice = input('Enter your choice: ')
    if choice == 'a' or choice == 'A':
        print('Addition')
        a = float(input('Enter first number:'))
        b = float(input('Enter second number:'))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print('Subtraction')
        a = float(input('Enter first number:'))
        b = float(input('Enter second number:'))
        sub(a, b)
    elif choice == 'C' or choice == 'c':
        print('Multiplication')
        a = float(input('Enter first number:'))
        b = float(input('Enter second number:'))
        mul(a, b)
    elif choice == 'D' or choice == 'd':
        print('Division')
        a = float(input('Enter first number:'))
        b = float(input('Enter second number:'))
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('Program ended')
        quit()
