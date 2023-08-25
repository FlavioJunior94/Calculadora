import calculadora
from time import sleep
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
        menu_base()
    if op==2:
        pass
    if op==3:
        pass
    if op==4:
        calculadora.menu()
    else:
        print("opção invalida!")
        sleep(1.8)
        menu_base()