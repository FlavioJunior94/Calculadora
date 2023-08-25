def numeros():
    while True:
        try:
            x=float(input('digite o primeiro numero: '))
            y=float(input('digite o segundo numero: '))
            break
        except:
            print('dados invalidos, tente novamente\n')
            continue
    return x,y
def soma(x):
    return print(f'resultado da soma: {sum(x)}')
def subtr():
    x,y=numeros()
    return print(f'resultado da subtração: {x-y}')
def multi():
    x, y = numeros()
    return print(f'resultado da multiplicação: {x*y}')
def divi():
    x, y = numeros()
    while y<=0:
        y = float(input('divisor deverá ser maior que 0: '))
    return print(f'resultado da divisão: {x/y}')
