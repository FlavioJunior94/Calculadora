import calculadora
from time import sleep
from utils import base
def decimal():
    pass

def menu_base():
    print("""
    ================================
    ====QUAL A BASE DO SEU VALOR====
    ==========FORNECIDO ?===========
    1 - DECIMAL
    2 - BINARIO
    3 - HEXAGONAL
    4 - VOLTAR AO MENU PRINCIPAL
    ================================
            """)
    while True:
        try:
            op=int(input('operação: '))
            break
        except:
            print('dado invalido! tente novamente.')

    if op==1:
        print('voce escolheu a opção 1')
        while True:
            try:
                num=int(input('Numero inteiro decimal: '))
                break
            except:
                print('valor incorreto, tente novamente !')
                continue
        print(f"""\nconversões:
 -Binario: {base.binario(num)}
 -Hexagonal: {base.hexadecimal(num)} """)
        sleep(1.8)
        menu_base()
    if op==2:
        num=input('Numero em Binario: ')
        if base.if_binario(num)==True:
            print(f"""\n
conversões:
 -decimal: {base.decimal(num)}
 -hexadecimal: {base.hexadecimal(base.decimal(num))}
            """)
            sleep(1.8)
            menu_base()
        else:
            print('O valor informado não é binario')
            sleep(1.8)
            menu_base()

    if op==3:
        num=input('Numero em Hexadecimal: ')
        if base.if_hexadecimal(num)==True:
            num =int(num,16)
            print(f"""\n
conversões:
 -decimal: {num}
 -binario: {base.binario(num)}
            """)
            sleep(1.8)
            menu_base()
        else:
            print('O valor informado não é binario')
            sleep(1.8)
            menu_base()
        pass
    if op==4:
        calculadora.menu()
    else:
        print("opção invalida!")
        sleep(1.8)
        menu_base()