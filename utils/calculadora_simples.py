from time import sleep
def main()->None:
    menu()

def menu():
    print("""
    ================================
    ======CALCULADORA SIMPLES=======
    ================================
    =======ESCOLHA A OPERAÇÃO=======
    ================================
    1 - ADIÇÃO
    2 - SUBTRAÇÃO
    3 - MULTIPLICAÇÃO
    4 - DIVISÃO
    5 - FECHAR CALCULADORA
    ================================
    """)
    while True:
        try:
            op=int(input('operação: '))
            break
        except:
            print('dado invalido! tente novamente.')

    if op==1:
        x,y=numeros()
        soma(x,y)
    elif op==2:
        x,y=numeros()
        subtr(x,y)
    elif op==3:
        x,y=numeros()
        multi(x,y)
    elif op==4:
        x,y=numeros()
        divi(x,y)
    elif op==5:
        pass
    else:
        print("opção invalida!")
        sleep(1.8)
        menu()

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

def soma(x,y):
    print(f'resultado da soma: {x+y}')
    sleep(1.8)
    menu()
def subtr(x,y):
    print(f'resultado da subtração: {x-y}')
    sleep(1.8)
    menu()
def multi(x,y):
    print(f'resultado da multiplicação: {x*y}')
    sleep(1.8)
    menu()
def divi(x,y):
    while y<=0:
        y = float(input('divisor deverá ser maior que 0: '))
    print(f'resultado da divisão: {x/y}')
    sleep(1.8)
    menu()

if __name__=='__main__':
    main()